import os
import sqlite3
import yaml
from enum import Enum

# Database
class QuestionStatus(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"

def create_connection(db_file: str) -> sqlite3.Connection:
  """ create a database connection to a SQLite database """
  conn = None
  try:
      conn = sqlite3.connect(db_file)
  except sqlite3.Error as e:
      print(e)
  return conn

def create_table(conn):
  """ create a table in the database """
  cursor = conn.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                      filename text,
                      author text,
                      text text,
                      reply_to text,
                      status text
                  )""")
  conn.commit()

def save_questions(conn : sqlite3.Connection, questions : list) -> None:
  """ save questions to the database """
  cursor = conn.cursor()
  for question in questions:
      cursor.execute("INSERT INTO questions VALUES (?,?,?,?,?)", 
                     (question.filename, question.author, question.text, question.reply_to, question.status.value))
  conn.commit()

def load_questions(conn : sqlite3.Connection) -> list:
  """ load questions from the database """
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM questions")
  rows = cursor.fetchall()
  questions = []
  for row in rows:
      question = Question(row[0], row[1], row[2], row[3], QuestionStatus(row[4]))
      questions.append(question)
  return questions

def update_question_status(conn : sqlite3.Connection, filename : str, status : QuestionStatus) -> None:
  """ update the status of a question in the database """
  cursor = conn.cursor()
  cursor.execute("UPDATE questions SET status = ? WHERE filename = ?", (status.value, filename))
  conn.commit()

class Question:
    def __init__(self, filename, author, text, reply_to, status=QuestionStatus.NEW, timestamp=None):
        self.filename = filename
        self.author = author
        self.text = text
        self.reply_to = reply_to
        self.status = status
        self.timestamp = timestamp

questions = []


def load_comments(data_dir: str, conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    for filename in os.listdir(data_dir):
        if filename.endswith(".yml"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
                # Check if the question already exists in the database
                cursor.execute("SELECT status FROM questions WHERE filename = ?", (filename,))
                db_status = cursor.fetchone()
                status = QuestionStatus(db_status[0]) if db_status else QuestionStatus.NEW
                timestamp = data.get('timestamp')
                questions.append(Question(
                    filename,
                    data.get('author'),
                    data.get('text'),
                    data.get('reply_to'),
                    status,
                    timestamp,
                ))

def get_new_question() -> Question:
    for question in questions:
        if question.status == QuestionStatus.NEW:
            return question
    return None

def decline_question(conn : sqlite3.Connection, question : Question) -> None:
    question.status = QuestionStatus.DECLINED
    reason = input("\x1b[31mReason for declining ? \x1b[0m:")
    question.reason = reason
    update_question_status(conn, question.filename, question.status)

    # Update YAML file with reason (optional)
    filepath = os.path.join(comments_dir, question.filename)
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    data['declined_reason'] = reason  # Add reason to YAML data
    with open(filepath, 'w') as f:
        yaml.dump(data, f)

     # Move file to declined directory (optional)
    os.rename(f"{comments_dir}/{question.filename}", f"{declined_comments_dir}/{question.filename}")

def accept_question(conn : sqlite3.Connection, question : Question) -> None:
    question.status = QuestionStatus.ACCEPTED
    update_question_status(conn, question.filename, question.status)

def print_question(question : Question) -> None:
    print(f"\x1b[33m{question.author}\x1b[0m submitted a question to \x1b[33m{question.reply_to}\x1b[0m on \x1b[33m{question.timestamp}\x1b[0m:")
    # Print question in light blue
    print(f"\x1b[36m{question.text}\x1b[0m")


def main() -> None:
    db_file = "student_questions.db"
    global comments_dir, declined_comments_dir
    comments_dir = "./_data/comments" 
    declined_comments_dir = "./_data/declined_comments" 
    conn = create_connection(db_file)

    if conn is not None:
        create_table(conn)  # Create the database table if it doesn't exist
        
        # Load questions from YAML files
        load_comments(comments_dir, conn)
        
        # Validate and save new questions to the database
        valid_questions = [q for q in questions]
        save_questions(conn, valid_questions)
        
        # Fetch new questions to review
        new_question = get_new_question()
        while new_question:
            print(new_question.status)
            print_question(new_question)
            
            user_action =  input("\x1b[32m[a] Accept\x1b[0m | \x1b[31m [d] Decline\x1b[0m : ")

            if user_action.lower() == 'a':
                accept_question(conn, new_question)

            elif user_action.lower() == 'd':
                decline_question(conn, new_question)

            else:
                print("Invalid action.")
            
            new_question = get_new_question()
        else:
            print("No new questions to review.")
            
        conn.close()

    else:
        print("Error: could not establish database connection.")

if __name__ == "__main__":
    main()

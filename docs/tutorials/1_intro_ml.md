---
layout: default
title: 1. Introduction to machine learning
nav_order: 4
parent : Tutorials
---

# Introduction to machine learning
{: .no_toc}


This chapter will teach you foundational concepts of machine learning (ML) through hands-on turorials.
The first three chapters only use interactive applications, no programming skills are required.
The fourth chapter reiterates the same concepts using programming tools that prevail in the ML industry, namely the Python programming language and dedicated ML libraries.
Lastly, the fifth section provides ressources to develop your on web-based interactive ML application, using the [Marcelle](https://www.marcelle.dev) toolkit.

{: .note-title }
> Tips
>
> We recommend to all attendants to follow the first four sections.

---

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Train your first image classifier

Have you ever trained a machine learning model ? If not, this is the right place to start.
First of all, what is a machine learning?

{: .note-title }
> Definition
>
> Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can effectively generalize from examples and thus perform tasks without explicit instructions.

In other words, machine learning (ML) part of the field of AI but its specificity lies in the fact that algorithms are learning from data.
To give you a concrete example, let's train your first image classifier from images collected with your webcam and using the application below.

[Train my first image classifier! ](/marcelle/ml-webcam){: .btn target="_blank"}

In this application, you can activate the `webcam` of your laptop on the left side of the screen. 
Below the `webcam`, you can choose a `label` to be associated with the images you will collect. Once the `label` selected, click on the button `hold to collect` to collect images with the corresponding `label`. Doing so, you will see the images you collect appearing in the `Training set` in the middle of the screen.
Reiterate this process for each `label` you want to collect images for. 

Once you finalized the creation of your `Training set` (images + corresponding labels), you can click on the button `Train` to train your image classifier.
Then, you can activate the `webcam` again and see the predictions of your image classifier in real-time in the component `Prediction confidence` on the bottom of the screen.

{: .note-title }
> Hints
>
> Take the time to test the model you trained. Try to trick its predictions and see how it reacts. What data could you add to the training set to improve its predictions?

You trained your first image classifier! Congratulations! 
But you don't know much about how machine learning works... Let's now see what's going on under the hood of this web application.

## The development cycle of ML

The development of ML is a cycle composed of 4 main steps. These steps are illustrated in the application below.

[The development cycle of ML](/marcelle/ml-vision){: .btn target="_blank"}



{: .note-title }

{: .note-title }

### Data collection

The first step of the development cycle of ML is data collection. It consists in collecting and annotating data samples that can be used by an ML algorithm to learn a mapping from inputs to outputs. In the previous example, the data samples are images collected with your webcam and the corresponding labels you provided.
If pairs of input and output are provided in the training set, we talk about **supervised learning**. If only inputs are provided, we talk about **unsupervised learning**.

The data samples are usually gathered in two sets: the **training set** and the **test set**. The training set is used to train the ML model, while the test set is used to evaluate the performance of the trained model. In other words, the training set is the exemples you work on during the semester, while the test set is the final exam.

We provide various miniature image datasets that represent classification problems in engineering, medecine, and public health:

- miniMASK: a dataset of 3 classes of images (with masks, without masks, and with masks incorrectly worn);
- miniROAD: a dataset of 3 classes or green, orange, and red traffic lights;
- miniTRASH: a dataset of 3 classes of images (packaging, transparent glass, and opaque glass);
- miniRETINA: a medical dataset of 3 classes of retinoscopic images (healthy, macular degeneration, and diabetic retinopathy);
- miniSKIN: a medical dataset of 2 classes of dermatoscopic images (benign and malignant skin lesions);

On the [`Data collection`](https://aica-wavelab.github.io/marcelle/ml-vision/#training) page, click on one button to select the dataset you want to work with for the rest of the tutorial.

{: .note-title }
> Hints
>
> Take the time observe each images (by clicking on the thumbnails). Are the differences between each classes obvious to you?



### Training

The training phase comprises three steps: 

2.1. **Features selection** : in our case, we will use a pre-trained neural network called MobileNet that extract 1024 features from images. These features were learned from a large dataset of images (ImageNet) and can be used to represent any image.

2.2. **Model selection** : Many machine learning models exist and were developed. In our case, we will use a model called multi-layer perceptron (MLP). It is a simple artificial neural network composed of an input layer (in our case, the 1024 features from MobileNe, some hidden layers that we can choose, and an output layer (the number of classes).
Two other parameters are important to set. The **batchSize** and the number of **epochs**. An artificial neural network can updates its neurons using several examples at the same time. The batch size indicates the number of images that will be used at each round to update the neurons. The number of epochs indicates the number of times the whole training set will be used to update the neurons. The higher the number of epochs, the more the model will be trained. However, if the number of epochs is too high, the model might overfit the training set and will not be able to generalize to new data. You can choose the number of hidden layers and neurons per layer, the batch size, and the number of epochs on the [`Training`](https://aica-wavelab.github.io/marcelle/ml-vision/#training) page of the application. 


2.3. **Training** : Click on the training button to start the neural network optimization.
You will then see two different learning curves appearing. The represent the losses and accuracies as a function of the number of epochs. The loss is a measure of the error between the predictions of the model and the true labels. The accuracy is the percentage of correct predictions. 
A validation loss and accuracy are computed using a portion of the training set that is not used for the training. 
If the validation loss and validation accuracy are not improving, it means that the model is overfitting the training set and that it will not generalize well to new data. In this case, you should stop the training and reflect on the parameters of the model or the data used for the task.

### Testing

At this point, the model only saw the training set, eventhough it artificially splited this set into a training and validation set. To really assess the model performance, we need to compute a test accuracy on unseen images. On the [`Testing`](https://aica-wavelab.github.io/marcelle/ml-vision/#training) page of the application, you can see two **confusion matrices**. On the left is shown the global accuracy and a confusion matrix computed on the training set only. The rows of the confusion matrix represent the true labels (what should be predicted), while the columns represent the predicted labels. The diagonal of the matrix represents the number of correct predictions. A confusion matrix gives a finer view of which class is confused with which class. 
On the left, you can see the global accuracy and a confusion matrix computed on the test set only. The test accuracy is a better indicator of the model performance. If the test accuracy is much lower than the training accuracy, it means that the model is overfitting the training set and that it will not generalize well to new data.

{: .note-title }

{: .note-title }
> Questions
>
> 1. For the task you selected, what averaged accuracy would you obtain with a random classifer? Is the trained classifier better than a random classifier in your case? 
> 2. What difference do you observe between the training and test accuracies? What does it mean?
> 3. Which classes are the most confused? Why do you think so? Among the confusions you identified, is there any would be more problematic than others in the problem selected? 
> 4. What would you do to improve the model performance?

### Deployment

Now you trained and test a machine learning model, you can learn more about its behavior by observing its predictions on particular images. On the [`Deployment`](https://aica-wavelab.github.io/marcelle/ml-vision/#training) page of the application, you can see the predictions of the model when you click on the thumbnails of the training or test set.
Machine learning models can be noisy and biased. **Noisiness** indicates that the model is not stable and that it can give different predictions for similar inputs (it's unpredictably wrong). **Bias** indicates that the model is wrong or unfair for similar inputs (it's always wrong in the same way). 
Biases in ML models can lead to discrimination as illustrated in many different controversies over the past years. These incidents are documented on a public website called [AI incident database](https://incidentdatabase.ai/cite/37/).

{: .note-title }
> Questions
>
> Among erroneous predictions, can you identify biases? Are these biases explained by the training data? Are these biases problematic in the problem selected?

Now you know the elementary steps to train and test a machine learning model, you can try the same process on another dataset. The next section will teach you how to conduct the same steps using a programming langage (Python) and dedicated ML libraries.

## Train your model in Python

In this section, you will learn how to train and test a machine learning model using Python and dedicated ML libraries. We recommand you to install Python via [Anaconda](https://www.anaconda.com/download). This way, you will also have jupyter notebook installed, which is a digital notebook that allows you to write and execute Python code in isolated cells. This way you can follow a step-by-step tutorial and execute the code at each step to see the results. You will also need yo install the following libraries: numpy, tensorflow, keras, matplotlib, and seaborn. You can install them using the following command in your terminal:

```bash
pip install numpy tensorflow keras matplotlib seaborn
```

The tutorial located in the file `ml-python-tutorial.ipynb` on the github repository of the course:

[Python tutorial](https://github.com/aica-wavelab/aica-project-workshop/tree/main/1_introduction/ml-vision-python){: .btn target="_blank"}

The end of the tutorial also explains how to import a model trained in the Marcelle application and use it in Python. 

## Create your own interactive ML web application

The interactive applications you used were programmed using Marcelle.
[Marcelle](https://marcelle.dev/) is a modular open source toolkit for programming interactive machine learning applications. Marcelle is built around components embedding computation and interaction that can be composed to form reactive machine learning pipelines and custom user interfaces. This architecture enables rapid prototyping and extension. Marcelle can be used to build interfaces to Python scripts, and it provides flexible data stores to facilitate collaboration between machine learning experts, designers and end users.

If you want to learn how to create your own interactive machine learning application, please read the [introduction](https://marcelle.dev/guide/) and follow the tutorial on the Marcelle website:

[Marcelle tutorial](https://marcelle.dev/guide/getting-started.html){: .btn target="_blank"}

---
layout: page
title: Instructors
description: Instructors that can help you for the implementation
nav_order: 10
---


# Scientific instructors

Scientific instructors prepared the technical content hosted on this website. They can guide you through the tutorials and your final project implementation.

{% assign instructors = site.staffers | where: 'role', 'Scientific instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

# Art and culture instructors

Artistic instructors can guide you through the artistic and cultural aspects of your project.

{% assign instructors = site.staffers | where: 'role', 'Artistic instructors' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

# AICA project leader

{% assign instructors = site.staffers | where: 'role', 'AICA project leader' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

# Teaching assistants

Students from HM and HMTM will also be present on-site to help organizing the course. 

{% assign instructors = site.staffers | where: 'role', 'Teaching assistant' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

<!-- 
# Lecturers

{% assign teaching_assistants = site.staffers | where: 'role', 'Lecturers and experts' %}
{% assign num_teaching_assistants = teaching_assistants | size %}

# Teaching assistants

{% if num_teaching_assistants != 0 %}
## Teaching Assistants
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %} -->

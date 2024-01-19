---
layout: page
title: Organizers
description: Organizers of the lecture series
nav_order: 10
---


# Organizers of the lecture series

{% assign instructors = site.staffers | where: 'name', 'Dr. Téo Sanchez (HM - MUC.DAI)' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign instructors = site.staffers | where: 'role', 'Artistic instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign instructors = site.staffers | where: 'role', 'AICA project leader' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}



# Student assistants


{% assign instructors = site.staffers | where: 'role', 'Teaching assistant' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
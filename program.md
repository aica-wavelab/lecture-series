---
layout: default
title: Program
description: Program of the lecture series
nav_order: 3
---

# Program


## Bloc 1: AI in music

{% assign sorted_speakers = site.speakers | where : "bloc", "AI in music" | sort: "talk_date" %}


| Speaker | Talk | Date | Submit your questions |
|:--------|:------|:-----|:-------------------|
{% for speaker in sorted_speakers %}| {{speaker.academic_title}} {{ speaker.name }} | {{ speaker.talk }} | {{speaker.talk_date | date: "%B %d, %Y"}} at {{ speaker.talk_date | date: "%H:%M" }} |[Questions](/lecture-series/speakers/{{ speaker.slug }}){: .btn } |
{% endfor %}


## Bloc 2: AI in visual and performing arts

{% assign sorted_speakers = site.speakers | where : "bloc", "AI in visual and performing arts" | sort: "talk_date" %}

| Speaker | Talk | Date | Submit your questions |
|:--------|:------|:-----|:-------------------|
{% for speaker in sorted_speakers %}| {{speaker.academic_title}} {{ speaker.name }} | {{ speaker.talk }} | {{speaker.talk_date | date: "%B %d, %Y"}} at {{ speaker.talk_date | date: "%H:%M" }} |[Questions](/lecture-series/speakers/{{ speaker.slug }}){: .btn } |
{% endfor %}



## Bloc 3: AI in the creative and cultural industries

{% assign sorted_speakers = site.speakers | where : "bloc", "AI in cultural and creative industries" | sort: "talk_date" %}

| Speaker | Talk | Date | Submit your questions |
|:--------|:------|:-----|:-------------------|
{% for speaker in sorted_speakers %}| {{speaker.academic_title}} {{ speaker.name }} | {{ speaker.talk }} | {{speaker.talk_date | date: "%B %d, %Y"}} at {{ speaker.talk_date | date: "%H:%M" }} |[Questions](/lecture-series/speakers/{{ speaker.slug }}){: .btn } |
{% endfor %}


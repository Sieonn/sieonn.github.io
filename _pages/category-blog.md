---
title: "GitHub Blog 만들기"
layout: archive
permalink: /blog

title: "Python"
layout: archive
permalink: /python
---

{% assign posts = site.categories.blog %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

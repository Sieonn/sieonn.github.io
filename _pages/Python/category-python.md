---
title: "Python"
layout: category
permalink: /python/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.python %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
{% assign posts = site.categories.samback %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
{% assign posts = site.categories.programmers %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

---
title: "GitHub Blog"
layout: category
permalink: /devlog/blog/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.blog %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

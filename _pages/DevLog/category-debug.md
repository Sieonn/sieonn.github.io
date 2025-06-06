---
title: "삽질 & 디버깅"
layout: category
permalink: /devlog/debug/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.debug %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

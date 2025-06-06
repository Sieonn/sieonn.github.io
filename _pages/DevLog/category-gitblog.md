---
title: "GitHub Blog"
layout: category
permalink: /devlog/gitblog/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.gitblog %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

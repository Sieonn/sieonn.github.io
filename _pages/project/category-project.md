---
title: "project"
layout: categories
permalink: /project/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

---
{% assign posts = site.categories.phobum %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

---

{% assign posts = site.categories.peauty %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}


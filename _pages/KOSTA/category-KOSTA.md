---
title: "KOSTA FullStack"
layout: default
permalink: /KOSTA/
category: kosta
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.java %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
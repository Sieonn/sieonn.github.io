---
title: "🌴01. 기초"
layout: category
permalink: /python/samback/one/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.one %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

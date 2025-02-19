---
title: "🌴기초 300제"
layout: archive
permalink: /python/samback/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.samback %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

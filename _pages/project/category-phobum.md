---
title: "PHOBUM"
layout: archive
category: phobum
permalink: /phobum/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.phobum %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

<!-- 공백이 있는 카테고리 같은경우 ['카테고리명']의 형식으로 만들어주기 -->

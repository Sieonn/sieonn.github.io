---
title: "기초 개념 정리"
layout: archive
category: basics
permalink: /frontend/basics/
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.basics %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

<!-- 공백이 있는 카테고리 같은경우 ['카테고리명']의 형식으로 만들어주기 -->

---
title: "클라우드 기본 사항"
layout: archive
category: Cloud Base
permalink: /Cloud Base/ 
author_profile: true
sidebar:
    nav: "sidebar-category"
---

{% assign posts = site.categories.Base %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}
<!-- 공백이 있는 카테고리 같은경우 ['카테고리명']의 형식으로 만들어주기 -->
---
title: "DB"
layout: archive
category: DB
permalink: /KOSTA/DB/
---

{% assign posts = site.categories.DB %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}

<!-- 공백이 있는 카테고리 같은경우 ['카테고리명']의 형식으로 만들어주기 -->

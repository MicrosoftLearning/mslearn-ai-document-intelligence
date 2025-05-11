---
title: Azure AI Document Intelligence Exercises
permalink: index.html
layout: home
---

The following exercises are designed to provide you with a hands-on learning experience in which you'll explore common tasks that developers do when building document intelligence solutions on Microsoft Azure.

> **Note**: To complete the exercises, you'll need an Azure subscription in which you have sufficient permissions and quota to provision the necessary Azure resources. If you don't already have one, you can sign up for an [Azure account](https://azure.microsoft.com/free). There's a free trial option for new users that includes credits for the first 30 days.

## Exercises

{% assign labs = site.pages | where_exp:"page", "page.url contains '/Instructions'" %}
{% for activity in labs  %}
{% if activity.url contains 'ai-foundry' %}
  {% continue %}
{% endif %}
<hr>
### [{{ activity.lab.title }}]({{ site.github.url }}{{ activity.url }})

{{activity.lab.description}}

{% endfor %}

> **Note**: While you can complete these exercises on their own, they're designed to complement modules on [Microsoft Learn](https://learn.microsoft.com/training/paths/extract-data-from-forms-document-intelligence/); in which you'll find a deeper dive into some of the underlying concepts on which these exercises are based.

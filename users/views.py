# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    body = """ 
                " <a href="{% url 'google_login' %}">
                <button class="btn btn-default half-width" type="button" > Google </button></a>"
           """
    c = get_template_from_string(body)


#!/bin/env python
# -*- coding: utf-8 -*-

# 2017/11/2 下午12:33

__author__ = 'li yangjin'

from . import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.hello),
]




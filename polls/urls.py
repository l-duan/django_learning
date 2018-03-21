# -*- coding:utf-8 -*-
__auth__ = 'christian'

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^index/$', views.index, name='index'),
]

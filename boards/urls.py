# -*- coding:utf-8 -*-
__auth__ = 'christian'

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path('^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]

# -*- coding:utf-8 -*-
__auth__ = 'christian'

from django.urls import path, re_path
from . import views

app_name = 'polls'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    # ex: /polls/5/
    re_path('^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    re_path('^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    re_path('^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# coding=UTF-8

from django.urls import path, re_path, include
from . import views

urlpatterns=[
    re_path(r'^$',views.setcookie),
    re_path(r'^hello/$',views.getcookie),
]
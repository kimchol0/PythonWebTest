from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.setsession),
    re_path(r'^get/$',views.getsession),
    re_path(r'^login/$',views.login),
    re_path(r'^usercenter/$', views.usercenter),
    re_path(r'^logintwo/$',views.logintwo),
    re_path(r'^usercentertwo/$', views.usercentertwo),
]
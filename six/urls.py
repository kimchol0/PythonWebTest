from django.contrib import admin
from django.http import request
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view()),
    re_path(r'^csrf/$',views.Index2View),

]
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^login/',views.IndexView.as_view()),
    re_path(r'^register/',views.RegisterView.as_view()),
]
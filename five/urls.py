from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view()),
    re_path(r'^query/$',views.Index2View.as_view()),
    re_path(r'^query1/$',views.Index3_View.as_view()),
]
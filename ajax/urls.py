from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view()),
    re_path(r'^get/$',views.GetView),
    re_path(r'^getajax/$',views.GetAjaxView),
    re_path(r'^only/$',views.OnlyView),
    re_path(r'^isExist/$',views.existView),
]
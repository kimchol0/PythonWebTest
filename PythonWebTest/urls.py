"""PythonWebTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^student/',include('student.url')),
    re_path(r'^one/',include('one.url')),
    re_path(r'^two/',include('two.urls')),
    re_path(r'^three/',include('three.urls')),
    re_path(r'^four/',include('four.urls')),
    re_path(r'^five/',include('five.urls')),
    re_path(r'^six/',include('six.urls')),
    re_path(r'^biaodan/',include('biaodan.urls')),
    re_path(r'^ajax/',include('ajax.urls')),
]

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def setcookie(request):
    response = HttpResponse()
    response.set_signed_cookie('uname','zhangsan',
                               salt='jksdfbhalefijk',
                               max_age=24*60*60)
    return response
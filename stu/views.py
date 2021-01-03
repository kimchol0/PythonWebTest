from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def setcookie(request):
    response = HttpResponse()
    response.set_signed_cookie('uname', 'zhangsan',
                               salt='jksdfbhalefijk',
                               max_age=24 * 60 * 60,
                               path='/student/hello/')
    response.delete_cookie('uname',path='/student/hello')
    return response
def getcookie(request):
    if 'uname' in request.COOKIES:
        uname = request.get_signed_cookie('uname',salt='jksdfbhalefijk')
        return HttpResponse(uname)
    else :
        return HttpResponse('当前Cookie信息不存在！')
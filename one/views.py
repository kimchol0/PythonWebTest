from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def setsession(request):
    #在session中存放数据（默认2周）
    request.session['uname']='zhangsan'
    #设置有效时间。参数类型：   整数：秒 设置0代表关闭浏览器之后过期  日期：指定日期值过期  None:默认时间过期
    request.session.set_expiry(3*24*60*60)
    request.session.flush()
    return HttpResponse('设置成功！')


def getsession(request):
    uname = request.session['uname']
    return HttpResponse(uname)
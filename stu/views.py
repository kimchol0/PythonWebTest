from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def setcookie(request):
    import datetime
    #创建响应对象
    response = HttpResponse()
    #将数据存储在cookie中。默认有效时间保存在浏览器缓存中，关闭浏览器数据丢失
    #
    response.set_cookie('uname','zhangsan',expires=datetime.datetime.today()+datetime.timedelta(days=2),path='/student/hello')
    return response
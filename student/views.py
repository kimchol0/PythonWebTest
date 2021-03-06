from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        # 判断request中是否存在'login'对应cookie信息
        if 'login' in request.COOKIES:
            # 'zhangsan,123'
            login = request.COOKIES.get('login', '').split(',')
            sname = login[0]
            spwd = login[1]
            return render(request, 'login.html', {'sname': sname, 'spwd': spwd})

        return render(request, 'login.html')
    else:
        # 获取请求参数
        sname = request.POST.get('sname')
        spwd = request.POST.get('spwd')
        flag = request.POST.get('flag')

        response = HttpResponse()

        # 判断是否登录成功
        if sname == 'zhangsan' and spwd == '123':
            response.content = '登录成功！'
            # 判断是否需要记住密码
            if flag:
                # 将用户名和密码存放至cookie中('zhangsan,123')
                response.set_cookie('login', sname + ',' + spwd, max_age=3 * 24 * 60 * 60, path='/student/login/')
            else:
                # 当不需要记住密码时，需要删除cookie中‘login’对应的数据
                response.delete_cookie('login', path='/student/login/')
        else:
            # 当登录失败时，需要删除cookie中‘login’对应的数据
            response.delete_cookie('login', path='/student/login/')
            # 重定向
            response.status_code = 302
            response.setdefault('Location', '/student/login/')

        return response
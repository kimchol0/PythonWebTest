from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def setsession(request):
    #在session中存放数据（默认2周）
    request.session['uname']='zhangsan'

    #输出cookie中的sessionid
    print(request.session.session_key)

    #设置有效时间。参数类型：   整数：秒 设置0代表关闭浏览器之后过期  日期：指定日期值过期  None:默认时间过期
    request.session.set_expiry(3*24*60*60)
    return HttpResponse('设置成功！')


def getsession(request):
    uname = request.session['uname']
    return HttpResponse(uname)


def login(request):
    if request.method=='GET':
        return render(request,'loginone.html')
    else:
        #接收请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        #判断
        if uname == 'zhangsan' and pwd=='123':
            request.session['login'] = uname
            return HttpResponseRedirect('/one/usercenter/')
        return HttpResponseRedirect('/one/login/')


def usercenter(request):
    #获取session中的数据
    uname = request.session['login']
    return render(request,'center.html',{'uname':uname})
    return None
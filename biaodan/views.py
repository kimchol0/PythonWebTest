from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import *

class IndexView(View):
    def get(self,request):
        loginform = Loginform()

        return render(request,'biaodanlogin.html',{'loginform':loginform})

    def post(self,request):
        loginform = Loginform(request.POST)
        #校验数据是否合法
        if loginform.is_valid():
            data = loginform.cleaned_data
            #和数据表中数据进行匹配
            user = authenticate(username=data['sname'],
                         password=data['spwd'])
            #判断是否登录成功
            if user:
                #将用户信息存放到session中
                login(request,user)
                return HttpResponse('登录成功')
        return HttpResponse('登录失败')
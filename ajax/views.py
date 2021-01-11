from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import *

class IndexView(View):
    def get(self,request):
        return render(request,'ajaxindex.html')


def GetView(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    print(uname,pwd)
    return JsonResponse({'flag':True})


def GetAjaxView(request):
    uname = request.GET.get('uname')
    print(uname)
    return JsonResponse({'flag':False})


def OnlyView(request):

    return render(request,'only.html')


def existView(request):
    #接收请求参数
    uname = request.GET.get('uname','')
    #判断数据库中是否存在
    stulist = Student.objects.filter(sname=uname)
    if stulist:
        return JsonResponse({'flag':True})
    return JsonResponse({'flag':False})
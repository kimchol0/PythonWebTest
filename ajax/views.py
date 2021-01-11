from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


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
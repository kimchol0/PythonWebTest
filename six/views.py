from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self,request):
        return render(request,'index4.html')
    def post(self,request):
        return HttpResponse('POST请求')
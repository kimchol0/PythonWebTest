from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self,request):
        content = "### 自定义过滤器"
        str = "abcdef"
        return render(request,'index2.html',{'c':content,'str':str})
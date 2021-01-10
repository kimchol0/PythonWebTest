from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Template, RequestContext
from django.views import View
from five.my_context_processors import getData


class IndexView(View):
    def get(self,request):
        return render(request,'index3.html')


class Index2View(View):
    def get(self,request):
        t = Template('{{uname}}')
        str = t.render(RequestContext(request,dict_= None,processors=(getData,)))
        return HttpResponse(str)
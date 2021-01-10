from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self,request):
        import datetime
        d = datetime.datetime.today()
        urlstr = '<h3>北京</h3>'
        return render(request,'index2.html',{'num':8,'str':'abcdef','d':d,'urlstr':urlstr})
from django.shortcuts import render

# Create your views here.
from django.views import View


class GetDataView(View):
    def get(self,request):
        import datetime
        return render(request,'getdata1.html',{'user':{'uname':'zhangsan'},
                                               'numlist':[1,2,3,4,5],
                                               'current':datetime.datetime.today(),
                                               'str':'hello',
                                               })
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class IndexView(View):
    def get(self,request):
        return render(request,'index4.html')
    def post(self,request):
        return HttpResponse('POST请求')

@csrf_protect
def Index2View(request):
    if request.method == 'GET':
            return render(request,'index4.html')
    return HttpResponse('Post...')
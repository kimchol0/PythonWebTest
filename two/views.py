from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')
    def post(self,request,*args,**kwargs):
        return HttpResponse('POST请求')


class StaticView(View):
    def get(self, request, *args, **kwargs):
        import re
        import os
        #获取文件名
        filepath = request.path
        m = re.match(r'/two/hello/(.*)',filepath)
        filename = m.group(1)
        filedir = os.path.join(os.getcwd(),'static\\images',filename)
        if not os.path.exists(filedir):
            raise Http404()
        # mimetypes
        # *.*表示匹配任意扩展名
        return FileResponse(open(filedir,'rb'),content_type='*/*')
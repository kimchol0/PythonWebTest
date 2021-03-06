from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):
    def process_request(self,request):
        print("中间件1")

    def process_view(self,request,view_func,view_func_args,
                     view_func_kwargs):
        #view_func对应views函数，view_func_args,kwargs对应views里的参数
        print("中间件1view")

    def process_response(self,request,response):
        print("中间件1返回")
        return response

#参数里的response就是views里面返回的值，所以要继续返回一下，否则客户端接收不到数据

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print("中间件2")

    def process_view(self,request,view_func,view_func_args,
                     view_func_kwargs):
        #view_func对应views函数，view_func_args,kwargs对应views里的参数
        print("中间件2view")

    def process_response(self,request,response):
        print("中间件2返回")
        return response

class Row3(MiddlewareMixin):
    def process_request(self,request):
        print("中间件3")

    def process_view(self,request,view_func,view_func_args,
                     view_func_kwargs):
        #view_func对应views函数，view_func_args,kwargs对应views里的参数
        print("中间件3view")

    def process_response(self,request,response):
        print("中间件3返回")
        return response
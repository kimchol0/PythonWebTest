from .models import *
def getData(request):
    return {'uname':'zhangsan'}

def getMenuInfo(request):
    #查询菜单表中的所有数据
    menus = Menu.objects.all().order_by('mid')
    return {'menu':menus}
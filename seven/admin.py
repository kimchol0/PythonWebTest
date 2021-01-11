from django.contrib import admin
from .models import BlogArticles
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    #显示表格列表字段
    list_display = ('title','author','publish',)
    #条件查询字段
    list_filter = ('publish','author',)
    #搜索框中根据某些字段进行查询
    search_fields = ('title','body')
    # 在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    raw_id_fields = ("author",)
    #以某个日期字段分层次查询
    date_hierarchy = 'publish'
    #排序字段
    ordering = ['publish','author']
admin.site.register(BlogArticles,BlogAdmin)


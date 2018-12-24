from django.contrib import admin

# Register your models here.
from app01 import models


#自定义展示的样式
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','pub_date')#展示的项目
    list_editable = ('name','price','pub_date')#可编辑
    filter_horizontal=('authors',)#数字选择作者

    list_per_page =3#每页展示数据的条数
    search_fields = ('id','name','publish__name')#搜索
    list_filter = ('pub_date','publish')#过滤
    ordering = ('-price','id')






admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.Book,BookAdmin)
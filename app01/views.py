from django.shortcuts import render,HttpResponse
from app01.models import *

# Create your views here.

import time,datetime
def show_time(request):
    t=datetime.datetime.now()
    # return HttpResponse("<html><body>It is now %s </body></html>" %t)

    return render(request,"show_time.html",{"time":t})




class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age

def query(request):

    l=["zhang","村长","书记"]
    zhangge=[]

    d={"name":"校长","age":5}
    c=Animal("alex",'公')

    test="hello world"
    num=100

    t=datetime.datetime.now()
    list=[]

    a="<a href='http://www.baidu.com' target='_blank'>click</a>"

    return render(request,"index.html",locals())


def login(request):
    user=request.POST.get('user')
    if user=='zhangge':
        print(user)
        return HttpResponse('ok')
    else:
        return HttpResponse('用户名错误')

def backend(request):
    return render(request, "base.html")

def student(request):
    student_list=["张三","李四",'王五']
    return render(request,"student.html",locals())



def index01(request):
    return render(request,'index01.html')



#单表操作

#b表记录的添加
def addbook(request):

    #方式一
    # b=Book(name="python基础",price=99,author="yuan",pub_date="2017-12-12")
    # b.save()

    #方式二
    Book.objects.create(name="老男孩linux",price=90,author="oldboy",pub_date="2017-12-12")
    # Book.objects.create(**dict)
    return HttpResponse("添加成功")

#表记录的修改
def update(request):
#方式一
    Book.objects.filter(author='yuan').update(price=990)
#方式二
    # b=Book.objects.get(author='oldboy')
    # b.price=100
    # b.save()
    return HttpResponse("修改成功")

def delete(request):
    Book.objects.filter(author='oldboy').delete()

    return HttpResponse("删除成功")


def select(request):
    # book_list=Book.objects.all()
    # print(book_list)
    # print(book_list[0])

    book_list = Book.objects.all()[:4]
    #book_list = Book.objects.get(id=1)#只能取出一条结果的时候才不报错
    ret=Book.objects.filter(author='yuan').values('name','price')#默认字典形式
    ret=Book.objects.filter(author='yuan').values_list('name','price')#列表形式
    book_list=Book.objects.exclude(author='yuan').values('name','price','author')#列表形式
    print(ret)


    #万能的双下划线__
    book_list=Book.objects.filter(price__gt=50).values('name','price')
    book_list=Book.objects.filter(name__icontains='P').values('name','price')
    return render(request,'index01.html',{"book_list":book_list})


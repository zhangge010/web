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


def addbook(request):
    b=Book(name="python基础",price=99,author="yuan",pub_date="2017-12-12")
    b.save()
    return HttpResponse("添加成功")
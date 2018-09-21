from django.shortcuts import render,HttpResponse

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
    print(user)
    return HttpResponse('ok')


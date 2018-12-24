from django.shortcuts import render,HttpResponse
from app01.models import *
from django.db.models import Avg,Min,Max,Sum,Count,Q,F

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
    Book.objects.create(name="老男孩linux",price=90,pub_date="2017-12-12",publish_id=1)
    # Book.objects.create(**dict)
    return HttpResponse("添加成功")

#表记录的修改
def update(request):
#方式一
    Book.objects.filter(price=90).update(price=990)
#方式二
    # b=Book.objects.get(author='oldboy')
    # b.price=100
    # b.save()
    return HttpResponse("修改成功")

def delete(request):
    Book.objects.filter(id=9).delete()
    # Publish.objects.filter(id=2).delete()

    return HttpResponse("删除成功")


def select(request):
    # book_list=Book.objects.all()
    # print(book_list)
    # print(book_list[0])

    # book_list = Book.objects.all()[:4]
    #book_list = Book.objects.get(id=1)#只能取出一条结果的时候才不报错
    # ret=Book.objects.filter(author='yuan').values('name','price')#默认字典形式
    # ret=Book.objects.filter(author='yuan').values_list('name','price')#列表形式
    # book_list=Book.objects.exclude(author='yuan').values('name','price','author')#列表形式
    # print(ret)


    #万能的双下划线__
    # book_list=Book.objects.filter(price__gt=60)
    # book_list=Book.objects.filter(pub_date__gt='2017-12-30')
    # book_list=Book.objects.filter(name__icontains='P').values('name','price')#模糊匹配
    # return render(request,'index01.html',{"book_list":book_list})


#正向查询
    # book_obj=Book.objects.get(name='linux')
    # print(book_obj.name)
    # print(book_obj.price)
    #
    #
    # print(book_obj.publish.name)
    # print(book_obj.publish.city)




#反向查询
#查询南京大学出版社出过的所有书籍的名字和价格
    # 方式一
    # pub_obj=Publish.objects.filter(name="南京大学出版社")[0]
    # ret=Book.objects.filter(publish=pub_obj).values_list('name','price')
    # print(ret)
#方式二
    # pub_obj=Publish.objects.filter(name="深圳出版社")[0]
    # print(pub_obj.book_set.all().values_list('name','price'))
    # for b in pub_obj.book_set.all():
    #     print(b.name,b.publish.name,b.price)
    # print(type(pub_obj.book_set.all()))
    # for a in pub_obj.book_set.all().values_list('name','price'):
    #     if a[1]>80:
    #         print(a)
#方式三
    # ret=Book.objects.filter(publish__name="南京出版社").values('name','price')
    # print(ret)
    #
    # #python出版社的名字
    # ret2=Publish.objects.filter(book__name='python').values('name')
    # print(ret2)
    # ret3=Book.objects.filter(name='python').values('publish__name')
    # print(ret3)
    #
    # # 南京的出版社出的所有的书
    # ret4=Book.objects.filter(publish__city='南京')
    # print("南京出版的书%s"% ret4)




    #通过对象的方式绑定关系
    # book_obj=Book.objects.get(id=1)
    # print(book_obj.authors.all().values('name','age'))
    # print(type(book_obj.authors.all()))
    #
    #
    #
    # author_obj=Author.objects.get(id=2)
    # print(author_obj.book_set.all().values_list('name','publish__name','price'))


#给id=4的书绑定添加所有的作者
    # book_obj=Book.objects.get(id=4)
    # author_obj=Author.objects.all()
    # book_obj.authors.add(*author_obj)

# 给id=4的书解除id=2的作者
#     a=Author.objects.filter(id=2)
#     book_obj.authors.remove(*a)




#创建第三张表，通过插入值的方式绑定关系
    # Book_Author.objects.create(book_id=2,author_id=2)
    #
    # book_obj=Book.objects.get(id=2)
    # print(book_obj.book_author_set.all()[0].author.name)
    # print(book_obj.book_author_set.all()[0].author.age)
    # print(book_obj.book_author_set.all()[0].author)



# 掌握通过filter和values里面的双下划线多对多的关联查询
#alex出过的书籍的名称以及价格
    # ret=Book.objects.filter(book_author__author__name="alex").values('name','price')
    # print(ret)

    # ret2=Book.objects.filter(authors__name='alex').values('name','price','publish__name')
    # print(ret2)


    #所有书的平均价格,aggregate
    # ret=Book.objects.all().aggregate(Avg('price'))
    # ret=Book.objects.all().aggregate(Sum('price'))
    # ret=Book.objects.filter(authors__name='alex').aggregate(alex_money=Sum('price'))
    # ret=Book.objects.filter(authors__name='alex').aggregate(alex_count=Count('name'))
    #
    # print(ret)
    #

    # ret=Book.objects.values('authors__name').annotate(Sum('price'))
    # print(ret)


    # ret=Publish.objects.values('name').annotate(Min('book__price'))
    # print(ret)

    # ret=Book.objects.filter(name='python',price=50).values('name','price','publish__name')
    # ret = Book.objects.get(name='python', price=50)

    # Book.objects.all().update(price=F('price')-20)
    # print(ret)

    # ret=Book.objects.filter(Q(price=30)|Q(name='python')).values('name','authors__name','publish__name')
    ret=Book.objects.filter(Q(price=30))
    # if ret.exists():
    #     print('ok')



    # print(ret)
    ret=ret.iterator()
    # a=ret.__next__()

    for i in ret:
        print(i.name,i.price,i.pub_date,i.publish.name)
    # print(ret.__next__())
    # for i in ret:
    #     print(i.name)
    # for i in ret:
    #     print(i.name)



    return render(request,'index01.html',locals())

f



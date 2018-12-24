from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=20,verbose_name='姓名')
    price=models.IntegerField('价格',null=True)
    # price = models.DecimalField(max_digits=5,decimal_places=2)
    pub_date=models.DateField()
    # author=models.CharField(max_length=32,null=False)
    #一对多
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE,)
    #创建多对多的关系（推荐）
    authors=models.ManyToManyField("Author")


    def __str__(self):
        return self.name
#手动创建第三张表
# class Book_Author(models.Model):
#     book=models.ForeignKey("Book",on_delete=models.CASCADE,)
#     author=models.ForeignKey("Author",on_delete=models.CASCADE,)



class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)
    def __str__(self):
        return self.name


class Publish(models.Model):

    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    def __str__(self):
        return self.name
from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default="0")
    telephone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=60,unique=True,default="0")
    password = models.CharField(max_length=20, default="0")
    regist_time = models.CharField(max_length=50, default="0")

    class Meta:
        db_table = 'User'


class Furn(models.Model):
    fid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50, default="0")
    fprice = models.FloatField()
    fcategory = models.CharField(max_length=20)
    fnum = models.IntegerField()
    fphoto = models.ImageField(upload_to='furnphoto')
    fdescribe = models.CharField(max_length=500, default="无")
    fsale = models.IntegerField(default=0)

    class Meta:
        db_table = 'Furn'


class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    rname = models.CharField(max_length=20, default="0")
    raddress = models.CharField(max_length=50, default="0")
    rphone = models.CharField(max_length=20, default="0")
    pay = models.FloatField()
    paystate = models.BooleanField(default=False)
    order_time = models.CharField(max_length=50, default="0")

    class Meta:
        db_table = 'Order'


class OrderItem(models.Model):
    o_oid = models.IntegerField(default=0)
    o_fid = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="0")
    price = models.FloatField(default=0.0)
    category = models.CharField(max_length=20, default="其他")
    num = models.IntegerField(default=0)
    buynum = models.IntegerField(default=0)

    class Meta:
        db_table = 'OrderItem'


class LookItem(models.Model):
    kid = models.AutoField(primary_key=True)
    uid = models.IntegerField(default=0)
    fid = models.IntegerField(default=0)
    date = models.DateField(default="0")
    lname = models.CharField(max_length=50, default="0")
    lprice = models.FloatField(default=0.0)
    lcategory = models.CharField(max_length=20, default="其他")

    class Meta:
        db_table = 'LookItem'
from django.db import models
from django.db import models
from django.contrib.auth.models import User

class DETAIL(models.Model):

    image = models.ImageField(upload_to="images", blank=True, null=True)
    detail=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    product_name=models.CharField(max_length=100,default="")
    final=models.IntegerField(default=0)
    type=models.CharField(max_length=100,default="")

class Cart(models.Model):
    username =models.CharField(max_length=100,default="")
    product_id=models.CharField(max_length=100,default="")
    quantity=models.IntegerField(default=0)
    total_cost=models.IntegerField(default=0)
    userid=models.CharField(max_length=100,default="")
    unique=models.IntegerField(default=0)
    
class about(models.Model):
    insta=models.CharField(max_length=100,default="")
    twit=models.CharField(max_length=100,default="")
    face=models.CharField(max_length=100,default="")
    favourite=models.CharField(max_length=100,default="")
    images = models.ImageField(upload_to="images", blank=True, null=True)


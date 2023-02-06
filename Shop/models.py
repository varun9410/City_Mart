from email.policy import default
from enum import unique
from django.contrib.auth.models import User
from django.db import models
import uuid
class Category(models.Model):
  category_name=models.CharField(max_length = 50 ,default='')
  def __str__(self):
    return self.category_name

class Product(models.Model):
  id = models.AutoField(unique=True,primary_key=True)
  name=models.CharField(max_length = 200)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
  sub_category=models.CharField(max_length = 200,default='')
  mrp=models.IntegerField(default=0)
  price=models.IntegerField(default=0)
  pub_date=models.DateField(auto_now=True)
  image=models.ImageField(upload_to="product_image/images",default='')
  inventory=models.IntegerField(default=1)
  def __str__(self):
    return self.name
class Review(models.Model):
  Product_id=models.ForeignKey(Product,on_delete=models.CASCADE,)
  User_id=models.ForeignKey(User,on_delete=models.CASCADE,)
  post_time=models.DateField(auto_now=True)
  review=models.CharField(max_length = 400,default='')
  rating=models.IntegerField(default=0)

  
class Contact(models.Model):
  Name=models.CharField(max_length = 200)
  Email=models.EmailField()
  Subject=models.CharField(max_length = 200,default='')
  Message=models.CharField(max_length = 400)
  def __str__(self):
    return self.Name

  
class rating(models.Model):
  Product=models.ForeignKey(Product,on_delete=models.CASCADE)
  User_id=models.ForeignKey(User,on_delete=models.CASCADE)
  rating=models.IntegerField(default=0)
  date=models.DateField(auto_now=True)

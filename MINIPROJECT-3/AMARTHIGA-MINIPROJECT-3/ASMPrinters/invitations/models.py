from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=50, default = '')
    add = models.CharField(max_length=50, default = '')
    pincode = models.IntegerField(default='')
    email= models.CharField(max_length=50, default = '')
    phone =models.BigIntegerField(default='')
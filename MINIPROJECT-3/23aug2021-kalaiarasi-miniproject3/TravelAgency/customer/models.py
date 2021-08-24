from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    mobnum=models.BigIntegerField()
    tripid=models.IntegerField()
    tripcost=models.IntegerField()
    tripplan=models.CharField(max_length=50)
    
    

from django.db import models

# Create your models here.
class Shop(models.Model):
    shopname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    emailID=models.CharField(max_length=100)
    website=models.CharField(max_length=100)
    phno=models.BigIntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)

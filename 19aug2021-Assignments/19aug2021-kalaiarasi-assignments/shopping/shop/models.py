from django.db import models

# Create your models here.
class Shop(models.Model):
    Shopname=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Emailid=models.CharField(max_length=50)
    MobNum=models.IntegerField()
    Username=models.CharField(max_length=50)
    Password=models.IntegerField()
    ConfirmPassword=models.IntegerField()

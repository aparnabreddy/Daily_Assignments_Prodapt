from django.db import models

# Create your models here.
class Shop(models.Model):
    Shopname=models.CharField(max_length=50)
    Adress=models.CharField(max_length=50)
    Emailid=models.CharField(max_length=50)
    Website=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Confirmpassword=models.CharField(max_length=50)

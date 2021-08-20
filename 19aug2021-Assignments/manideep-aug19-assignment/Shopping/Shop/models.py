from django.db import models

# Create your models here.


class Shop(models.Model):
    shopname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
from django.db import models
# Create your models here.
class Product(models.Model):
    prname=models.CharField(max_length=50)
    prdesc=models.CharField(max_length=50)
    prprice=models.BigIntegerField()
    prmanfd=models.CharField(max_length=50)
    prbrand=models.CharField(max_length=50)
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    details=models.CharField(max_length=50)
    sellername=models.CharField(max_length=20)
    manuname=models.CharField(max_length=50)
    manudate=models.IntegerField()
    expdate=models.IntegerField()
    
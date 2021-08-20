from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=50)
    detail=models.CharField(max_length=50)
    sellername=models.CharField(max_length=50)
    manfname=models.CharField(max_length=50)
    mfgdate=models.IntegerField()
    expdate=models.IntegerField()
    price=models.IntegerField()
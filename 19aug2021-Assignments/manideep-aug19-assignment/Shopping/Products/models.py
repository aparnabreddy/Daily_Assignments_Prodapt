from django.db import models

# Create your models here.

class product(models.Model):
    productname=models.CharField(max_length=50)
    productdes=models.CharField(max_length=100)
    sellername=models.CharField(max_length=50)
    manufracturename=models.CharField(max_length=50)
    price=models.BigIntegerField()
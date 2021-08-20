from django.db import models

# Create your models here.

class Seller(models.Model):
    sellername=models.CharField(max_length=50)
    add=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phn=models.BigIntegerField()
    district=models.CharField(max_length=50)
    age=models.IntegerField()
    adhar=models.BigIntegerField()
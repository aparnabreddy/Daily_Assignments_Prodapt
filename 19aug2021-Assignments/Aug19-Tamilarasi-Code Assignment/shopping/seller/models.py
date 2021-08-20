from django.db import models

# Create your models here.
class Seller(models.Model):
    sname=models.CharField(max_length=50)
    saddress=models.CharField(max_length=50)
    smailid=models.CharField(max_length=50)
    sphoneno=models.BigIntegerField()
    sdistrict=models.CharField(max_length=20)
    sage=models.IntegerField()
    saadhar=models.BigIntegerField()



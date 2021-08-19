from django.db import models

# Create your models here.

class product(models.Model):
    pname=models.CharField(max_length=50)
    pdes=models.CharField(max_length=100)
    sname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    price=models.BigIntegerField()

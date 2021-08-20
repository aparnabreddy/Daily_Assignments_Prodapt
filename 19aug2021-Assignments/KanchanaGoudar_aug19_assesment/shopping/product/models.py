from django.db import models

# Create your models here.
class Product(models.Model):
    Pname=models.CharField(max_length=50)
    Pdetails=models.CharField(max_length=50)
    Sname=models.CharField(max_length=50)
    Mname=models.CharField(max_length=50)
    Mdate=models.CharField(max_length=50)
    Edate=models.CharField(max_length=50)
    Price=models.IntegerField()

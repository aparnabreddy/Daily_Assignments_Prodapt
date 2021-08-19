from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=50)
    pdetails=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    price=models.IntegerField()

    
    

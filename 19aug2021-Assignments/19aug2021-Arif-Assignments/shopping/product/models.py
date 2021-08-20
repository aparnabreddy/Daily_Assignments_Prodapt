from django.db import models
class Product(models.Model):
   Productname=models.CharField(max_length=25)
   Productdetails=models.CharField(max_length=50)
   Sellername=models.CharField(max_length=50)
   Manufacturename=models.CharField(max_length=25)
   price=models.IntegerField()
   Manufacturingdate =models.CharField(max_length=25)
   Expirydate=models.CharField(max_length=25)
   

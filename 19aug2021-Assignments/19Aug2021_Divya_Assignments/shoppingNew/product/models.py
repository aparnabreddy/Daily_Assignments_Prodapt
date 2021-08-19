from datetime import datetime
from django.db import models

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length=50)
    Product_Details = models.CharField(max_length=50)
    Seller_Name = models.CharField(max_length=50)
    BRAND = models.CharField(max_length=50)
    Manufacturer_Name = models.CharField(max_length=50)
    Manufacturing_Date = models.CharField(max_length=50)
    #Expire_Date = models.DateTimeField(default=datetime.now())
    Price = models.IntegerField(default=False)

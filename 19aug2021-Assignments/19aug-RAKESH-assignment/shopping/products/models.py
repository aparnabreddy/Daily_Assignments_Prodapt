from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_details=models.CharField(max_length=100)
    seller_name=models.CharField(max_length=100)
    manufacturer_name=models.CharField(max_length=100)
    manufacturing_date=models.CharField(max_length=50)
    expiry_date=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    brands=models.CharField(max_length=100)

from django.db import models
class Product(models.Model):
    Productname=models.CharField(max_length=50)
    Productdetails=models.CharField(max_length=50)
    Sellername=models.CharField(max_length=50)
    ManufactureName=models.CharField(max_length=50)
    ManufactureDate=models.IntegerField()
    ExpiryDate=models.IntegerField()
    Branch=models.CharField(max_length=50)
    
    

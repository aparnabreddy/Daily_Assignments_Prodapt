from django.db import models

# Create your models here.
# "productname","discription","price","manufacturer","manufacturingdate","expirydate"
class Items(models.Model):
    productname = models.CharField(max_length=200)
    discription = models.CharField(max_length=500)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=200)
    manufacturingdate = models.DateField()
    expirydate= models.DateField()
    
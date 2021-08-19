from django.db import models

# Create your models here.
class Seller(models.Model):
    Seller_Name = models.CharField(max_length=50)
    Seller_Address = models.CharField(max_length=50)
    EMail_Id = models.CharField(max_length=50)
    Phone_Number = models.BigIntegerField(default=False)
    Date_of_Birth = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Age = models.IntegerField(default=False)
    Adhar_Number = models.BigIntegerField(default=False)
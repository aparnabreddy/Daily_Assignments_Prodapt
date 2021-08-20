from django.db import models

# Create your models here.
class Seller(models.Model):
    seller_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    emailID=models.CharField(max_length=100)
    phno=models.BigIntegerField()
    dob=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    age=models.IntegerField()
    aadhar_no=models.BigIntegerField()
    
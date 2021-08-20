from django.db import models

# Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    phoneno=models.BigIntegerField()
    dateofbirth=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    age=models.IntegerField()
    aadhar=models.BigIntegerField()
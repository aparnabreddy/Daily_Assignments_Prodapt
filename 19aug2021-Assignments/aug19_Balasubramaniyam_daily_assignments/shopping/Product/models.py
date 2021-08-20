from django.db import models

# Create your models here.
class Productmodel(models.Model):
    pname=models.CharField(max_length=50)
    pdetails=models.CharField(max_length=50)
    sellername=models.CharField(max_length=50)
    manufacturedate=models.DateField()
    expirydate=models.DateField()

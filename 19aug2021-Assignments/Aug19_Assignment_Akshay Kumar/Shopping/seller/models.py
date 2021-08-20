from django.db import models

class Seller(models.Model):
    selname = models.CharField(max_length=50)
    seladdress = models.CharField(max_length=50)
    selemail = models.CharField(max_length=50)
    selphno = models.BigIntegerField()
    seldob = models.CharField(max_length=50)
    seldistrict = models.CharField(max_length=50)
    selage = models.IntegerField()
    selaadhar = models.BigIntegerField()
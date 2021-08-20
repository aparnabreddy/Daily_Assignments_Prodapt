from django.db import models

class Products(models.Model):
    prodname = models.CharField(max_length=50)
    proddetails = models.CharField(max_length=50)
    selname = models.CharField(max_length=50)
    manfname = models.CharField(max_length=50)
    manfdate = models.CharField(max_length=50)
    expdate = models.CharField(max_length=50)
    price = models.IntegerField()

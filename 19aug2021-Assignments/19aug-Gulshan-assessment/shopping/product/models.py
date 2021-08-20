from django.db import models

# Create your models here.


class product(models.Model):
    proname = models.CharField(max_length=50)
    procode = models.IntegerField()
    prodescription =models.CharField(max_length=50)
    proprice = models.IntegerField()
    # seller_name = models.CharField(max_length=20)
    # manufacturer_name=models.CharField(max_length=20)
    
    
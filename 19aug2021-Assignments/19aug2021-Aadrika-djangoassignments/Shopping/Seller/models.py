from django.db import models

# Create your models here.
class Seller(models.Model):
    selname=models.CharField(max_length=50)
    seladd=models.CharField(max_length=50)
    selphone=models.BigIntegerField()
    selemail=models.CharField(max_length=50)
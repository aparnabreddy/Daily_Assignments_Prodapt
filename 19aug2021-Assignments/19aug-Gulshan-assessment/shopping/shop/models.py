from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Shop(models.Model):
    Shopname = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    

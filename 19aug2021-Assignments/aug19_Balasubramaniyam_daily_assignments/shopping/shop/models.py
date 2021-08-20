from django.db import models

# Create your models here.
class ShopModel(models.Model):
    sname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.CharField(max_length=50)
    phone=models.BigIntegerField()


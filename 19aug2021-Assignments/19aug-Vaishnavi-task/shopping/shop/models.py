from django.db import models

class Shopapp1(models.Model):
    shop_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    website=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    user=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    
   


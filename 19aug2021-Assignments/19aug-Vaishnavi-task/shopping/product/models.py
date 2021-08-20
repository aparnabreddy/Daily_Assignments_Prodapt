from django.db import models

class Productapp1(models.Model):
    product_name = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=20)
    manufacturer_name=models.CharField(max_length=20)
    


from django.db import models

class Sellerapp1(models.Model):
    seller_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email_id = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    Dob=models.DateTimeField()
    district=models.CharField(max_length=200)
    age=models.DateTimeField()
    adhar=models.BigIntegerField()
   

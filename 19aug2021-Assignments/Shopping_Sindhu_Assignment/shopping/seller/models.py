from django.db import models

# # Create your models here.
class Seller(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phoneno=models.BigIntegerField()
    district=models.CharField(max_length=50)
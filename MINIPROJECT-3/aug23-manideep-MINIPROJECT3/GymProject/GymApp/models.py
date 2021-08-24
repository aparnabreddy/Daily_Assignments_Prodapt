from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    mobilenumber=models.BigIntegerField()
    email=models.CharField(max_length=100)
    date=models.DateField()
    adharno=models.BigIntegerField()
    trainingtype=models.CharField(max_length=100)
    
    
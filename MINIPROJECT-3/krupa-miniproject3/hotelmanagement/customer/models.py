from django.db import models

# Create your models here.

class customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    mbno=models.CharField(max_length=50)
    adharno=models.CharField(max_length=50)
    checkin=models.CharField(max_length=50)
    checkout=models.CharField(max_length=50)
    roomno=models.CharField(max_length=50)
    

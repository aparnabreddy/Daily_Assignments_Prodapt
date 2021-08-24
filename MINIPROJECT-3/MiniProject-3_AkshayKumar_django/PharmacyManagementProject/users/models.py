from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pincode = models.IntegerField()
    phone = models.BigIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

from django.db import models

# Create your models here.
class User(models.Model):
    Ucode=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Mobileno=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

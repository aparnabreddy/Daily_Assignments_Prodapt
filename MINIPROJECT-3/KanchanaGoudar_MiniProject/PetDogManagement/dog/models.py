from django.db import models

# Create your models here.
class Dog(models.Model):
    Dogid=models.CharField(max_length=50)
    Dname=models.CharField(max_length=50)
    Dage=models.CharField(max_length=50)
    Dprice=models.CharField(max_length=50)
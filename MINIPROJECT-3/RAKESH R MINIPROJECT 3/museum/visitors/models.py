
from django.db import models

# Create your models here.
class Visitors(models.Model):
    name=models.CharField(max_length=100)
    ticketno=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phno=models.CharField(max_length=50)
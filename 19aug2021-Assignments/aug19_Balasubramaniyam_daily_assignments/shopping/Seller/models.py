from django.db import models
from django.utils.timezone import now
import datetime

t= datetime.datetime.now()
# Create your models here.
class Sellermodel(models.Model):
    name=models.CharField(max_length=50,default=None)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    date=models.DateTimeField(default=now)
    district=models.CharField(max_length=50)
    adhar=models.CharField(max_length=50)
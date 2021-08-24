from django.db import models

class Medicines(models.Model):
    rackno = models.CharField(max_length=50)
    medname = models.CharField(max_length=50)
    medcat = models.CharField(max_length=50)
    mfgdate = models.DateField()
    expdate = models.DateField()
    cost = models.IntegerField()
    stock = models.IntegerField()



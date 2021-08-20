from django.db import models

class Shop(models.Model):
    sname = models.CharField(max_length=50)
    saddress = models.CharField(max_length=50)
    semail = models.CharField(max_length = 50)
    sweb = models.CharField(max_length = 50)
    sphone = models.CharField(max_length=50)
    susername = models.CharField(max_length=50)
    spwd = models.CharField(max_length=50)
    scpwd = models.CharField(max_length=50)



from django.db import models

# Create your models here.
class Shop(models.Model):
    Shop_Name= models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    email_Id= models.CharField(max_length=50)
    USER_NAME= models.CharField(max_length=50)
    PASSWORD = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    phn_no= models.BigIntegerField()

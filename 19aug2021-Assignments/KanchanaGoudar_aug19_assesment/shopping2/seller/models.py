from django.db import models

# Create your models here.
class Seller(models.Model):
    Sname=models.CharField(max_length=50)
    Adress=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Date_of_birth=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Age=models.CharField(max_length=50)
    Adharnumber=models.CharField(max_length=40)
from django.db import models

# Create your models here.
class Seller(models.Model):
    sellername=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Emailid=models.CharField(max_length=50)
    MobNum=models.BigIntegerField()
    DOB=models.IntegerField()
    Age=models.IntegerField()
    AdhaarNum=models.IntegerField()
    District=models.CharField(max_length=50)
    

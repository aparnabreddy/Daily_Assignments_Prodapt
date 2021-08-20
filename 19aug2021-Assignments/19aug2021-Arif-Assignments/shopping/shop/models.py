from django.db import models
class Shop(models.Model):
   shopname=models.CharField(max_length=25)
   Address=models.CharField(max_length=50)
   emailid=models.CharField(max_length=50)
   website=models.CharField(max_length=25)
   phoneno=models.BigIntegerField()
   username=models.CharField(max_length=25)
   password=models.CharField(max_length=25)
   confirmpassword=models.CharField(max_length=25)
   #register=models.CharField()

from django.db import models
class Brand(models.Model):
   username=models.CharField(max_length=25)
   password =models.CharField(max_length=50)

   
   Country =models.CharField(max_length=25)


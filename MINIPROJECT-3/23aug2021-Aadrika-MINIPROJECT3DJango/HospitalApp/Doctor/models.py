from django.db import models
# Create your models here.
class Doctors(models.Model):
    dname=models.CharField(max_length=50)
    dadd=models.CharField(max_length=50)
    dspecial=models.CharField(max_length=50,default="dentist")
    dcont=models.BigIntegerField(default=0)
    dcity=models.CharField(max_length=50,default='bhopal')
    demail=models.CharField(max_length=50,default="hospital@bansal.com")
    
    

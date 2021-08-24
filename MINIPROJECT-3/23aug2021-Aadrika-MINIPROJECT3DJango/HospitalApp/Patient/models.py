from django.db import models
# Create your models here.
class Patients(models.Model):
    pname=models.CharField(max_length=50)
    padd=models.CharField(max_length=50)
    pdob=models.CharField(max_length=50)
    pbg=models.CharField(max_length=50)
    pcity=models.CharField(max_length=50,default="bhopal")
    pemail=models.CharField(max_length=50,default="patient.mmail")
    pphone=models.CharField(max_length=50)
    
    

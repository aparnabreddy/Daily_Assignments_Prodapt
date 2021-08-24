from django.db import models
class Movies(models.Model):
    city=models.CharField(max_length=50,default='')
    mname=models.CharField(max_length=50,default='')
    mduration=models.CharField(max_length=50,default='')
    mtimings=models.CharField(max_length=50,default='')
    totalseats=models.CharField(max_length=50,default='')
    audi=models.CharField(max_length=50,default='')
    
#{"city":"Bhopal","mname":"shershah","mduration":"2 hrs","mtimings":"["12pm,3pm,6pm"]","totalseats":"100","audi":"PVR"}

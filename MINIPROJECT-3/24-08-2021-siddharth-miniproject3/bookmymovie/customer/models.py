from django.db import models
class Customers(models.Model):
  
    name=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    ntickets=models.CharField(max_length=50)
    timings=models.CharField(max_length=50)
    audi=models.CharField(max_length=50)
    seatnum=models.CharField(max_length=50)

    
    
    
#{"name":"Siddharth","mname":"Shershah","ntickets":"2","timing":3 pm,"audi":"PVR","seatnum":"1"}

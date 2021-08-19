from django.db import models
class Sellers(models.Model):
    sellername=models.CharField(max_length=50,default='')
    address=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=50,default='')
    dob=models.CharField(max_length=50,default='')
    district=models.CharField(max_length=50,default='')
    age=models.CharField(max_length=50,default='')
    aadharnum=models.CharField(max_length=50,default='')
#{"sellername":"raju","address":"bhopal","email":"raju@gmail.com","phone":"9425171349","dob":"15/12/1998","district":"sagar","age":"21","aadharnum":"34256627"}
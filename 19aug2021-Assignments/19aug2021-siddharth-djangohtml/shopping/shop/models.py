from django.db import models
class Shops(models.Model):
    shopname=models.CharField(max_length=50,default='')
    saddress=models.CharField(max_length=50,default='')
    semail=models.CharField(max_length=50,default='')
    swebsite=models.CharField(max_length=50,default='')
    sphone=models.CharField(max_length=50,default='')
    susername=models.CharField(max_length=50,default='')
    spassword=models.CharField(max_length=50,default='')
    scpassword=models.CharField(max_length=50,default='')
#{"shopname":"Nikhar","saddress":"sagar","semail":"siddhugupta15@gmail.com","swebsite":"nikhar.com","sphone":"9425171349","susername":"nikhar15","spassword":"12345","scpassword":"12345"}
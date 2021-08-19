from django.db import models
class Products(models.Model):
    pname=models.CharField(max_length=50,default='')
    pdetail=models.CharField(max_length=50,default='')
    sname=models.CharField(max_length=50,default='')
    manfname=models.CharField(max_length=50,default='')
    manfdate=models.CharField(max_length=50,default='')
    expdate=models.CharField(max_length=50,default='')
    price=models.CharField(max_length=50,default='')
#{"pname":"cream","pdetail":"skin care","sname":"akash","manfname":"Joy","manfdate":"20/07/21","expdate":"20/07/23","price":"500"}
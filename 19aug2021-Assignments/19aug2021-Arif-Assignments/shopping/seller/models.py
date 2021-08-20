from django.db import models
class Seller(models.Model):
   sellername=models.CharField(max_length=25)
   address=models.CharField(max_length=50)
   email=models.CharField(max_length=50)
   phoneno=models.BigIntegerField()
   dob=models.CharField(max_length=25)
   district=models.CharField(max_length=25)
   age=models.IntegerField()
   adhaarno=models.BigIntegerField()

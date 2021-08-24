from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    mailid=models.CharField(max_length=60)
    examtype=models.CharField(max_length=50)
    fee=models.CharField(max_length=40)
    reg_date=models.CharField(max_length=40)
    reg_close_date=models.CharField(max_length=50)
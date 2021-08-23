from django.db import models

# Create your models here.

class roomrent(models.Model):
    roomclass=models.CharField(max_length=50)
    classprice=models.CharField(max_length=50)
    nigths=models.CharField(max_length=50)
    roomno=models.CharField(max_length=50)
    


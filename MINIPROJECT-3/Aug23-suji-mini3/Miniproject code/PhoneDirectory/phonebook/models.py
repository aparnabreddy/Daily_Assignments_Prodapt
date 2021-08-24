from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
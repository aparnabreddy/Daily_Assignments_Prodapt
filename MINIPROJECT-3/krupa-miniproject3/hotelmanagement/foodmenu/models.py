from django.db import models

# Create your models here.

class foodmenu(models.Model):
    breakfast=models.CharField(max_length=50)
    lunch=models.CharField(max_length=50)
    dinner=models.CharField(max_length=50)
    dessert=models.CharField(max_length=50)
    drinks=models.CharField(max_length=50)
    chats=models.CharField(max_length=50)
    


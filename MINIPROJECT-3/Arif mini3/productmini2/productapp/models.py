from django.db import models
class Product(models.Model):
    Maincourse=models.CharField(max_length=50)
    Starter=models.CharField(max_length=50)
    Dessert=models.CharField(max_length=25)
    

    
    

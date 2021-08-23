from django.db import models

# Create your models here.
class Vegitablesapp(models.Model):
    vegitable_code=models.IntegerField()
    name = models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    packing_date=models.DateField()
    expiry_date=models.DateField()
    price=models.IntegerField()
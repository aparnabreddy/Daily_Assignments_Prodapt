from django.db import models

# Create your models here.
class Bank(models.Model):
    customer_id=models.IntegerField()
    customer_name=models.CharField(max_length=50)
    deposit_amount=models.IntegerField()
    
from django.db import models

# Create your models here.
class Artifacts(models.Model):
    name=models.CharField(max_length=100)
    acode=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
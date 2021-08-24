from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Country(models.Model):
    Country_name = CharField(max_length=50)
    Gold_medal = IntegerField()
    Silver_medal = IntegerField()
    Bronze_medal = IntegerField()
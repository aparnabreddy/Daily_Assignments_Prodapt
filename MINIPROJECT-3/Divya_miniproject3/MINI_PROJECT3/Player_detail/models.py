from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Player(models.Model):
    Name = CharField(max_length=50)
    Game = CharField(max_length=50)
    Country = CharField(max_length=50)
    Place = IntegerField()
    Medal = CharField(max_length=50)
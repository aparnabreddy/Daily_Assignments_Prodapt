from django.db import models
from django.db.models import fields
from rest_framework import serializers
from shop.models import Shop

class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('Shopname','address','email','website','phone_number')

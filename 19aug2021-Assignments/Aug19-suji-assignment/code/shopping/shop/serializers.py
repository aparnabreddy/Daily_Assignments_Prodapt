from django.db import models
from django.db.models import fields
from rest_framework import serializers
from shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('shopname','address','emailid','website','phoneno','username','password','confirmpassword')
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from shop.models import Shopapp1

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shopapp1
        fields = ('shop_name','address','email','website','phone','user','password','cpassword')

        
   


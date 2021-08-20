from django.db import models
from django.db.models import fields
from rest_framework import serializers
from seller.models import Sellerapp1

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sellerapp1
        fields = ('seller_name','address','email_id','phone','district','age','adhar')
      
   
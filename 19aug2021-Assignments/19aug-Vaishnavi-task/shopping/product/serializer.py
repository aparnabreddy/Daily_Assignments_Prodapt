from django.db import models
from django.db.models import fields
from rest_framework import serializers
from product.models import Productapp1

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productapp1
        fields = ('product_name','product_detail','seller_name','manufacturer_name')
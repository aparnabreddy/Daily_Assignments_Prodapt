from django.db.models import fields
from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = ("Product_Name","Product_Details","Seller_Name","BRAND","Manufacturer_Name","Manufacturing_Date","Price")
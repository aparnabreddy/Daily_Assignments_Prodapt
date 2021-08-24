from rest_framework import serializers
from products.models import Items

class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Items 
        fields = ("productname","discription","price","manufacturer","manufacturingdate","expirydate")
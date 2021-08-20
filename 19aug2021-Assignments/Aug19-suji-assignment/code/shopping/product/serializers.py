from django.db import models
from django.db.models import fields
from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pname','detail','sellername','manfname','mfgdate','expdate','price')
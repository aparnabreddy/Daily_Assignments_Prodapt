from django.db.models import fields
from rest_framework import serializers
from Product.models import Productmodel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productmodel
        fields=('pname','pdetails','sellername','manufacturedate','expirydate')
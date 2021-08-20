from rest_framework import serializers
from product.models import Product

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('Pname','Pdetails','Sname','Mname','Mdate','Edate','Price')
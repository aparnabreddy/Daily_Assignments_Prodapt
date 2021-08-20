from rest_framework import serializers
from products.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('prodname','proddetails','selname','manfname','manfdate','expdate','price')
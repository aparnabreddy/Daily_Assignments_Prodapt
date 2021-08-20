from rest_framework import serializers
from products.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('product_name','product_details','seller_name','manufacturer_name','manufacturing_date','expiry_date','price','brands')
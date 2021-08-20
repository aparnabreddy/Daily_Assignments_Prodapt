from rest_framework import serializers
from product.models import Products
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=("pname","pdetail","sname","manfname","manfdate","expdate","price")
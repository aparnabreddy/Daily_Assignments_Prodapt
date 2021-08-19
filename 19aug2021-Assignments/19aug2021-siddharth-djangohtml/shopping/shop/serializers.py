from rest_framework import serializers
from shop.models import Shops
class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model=Shops
        fields=("shopname","saddress","semail","swebsite","sphone","susername","spassword","scpassword")
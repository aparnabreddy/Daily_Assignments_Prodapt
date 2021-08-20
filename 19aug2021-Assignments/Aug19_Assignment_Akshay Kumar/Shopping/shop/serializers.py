from rest_framework import serializers
from shop.models import Shop

class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('sname','saddress','semail','sweb','sphone','susername','spwd','scpwd')
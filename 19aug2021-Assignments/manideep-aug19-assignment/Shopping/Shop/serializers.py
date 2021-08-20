from rest_framework import serializers
from Shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('shopname','address','email','website','phone','username','password')
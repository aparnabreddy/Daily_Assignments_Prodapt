from rest_framework import serializers
from shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('shopname','address','emailID','website','phno','username','password','confirmpassword')
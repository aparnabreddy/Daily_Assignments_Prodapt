from rest_framework import serializers
from shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('name','address','emailid','website','phoneno','username','password')
        
        
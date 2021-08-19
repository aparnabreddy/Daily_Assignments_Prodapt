from rest_framework import serializers
from shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('Shopname','Address','Emailid','MobNum','Username','Password','ConfirmPassword')

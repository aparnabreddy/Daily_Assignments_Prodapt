from rest_framework import serializers
from shop.models import Shop

class ShopSerialize(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('Shopname','Adress','Emailid','Website','Phone','Username','Password','Confirmpassword')
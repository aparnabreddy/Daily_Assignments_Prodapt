from django.db.models import fields
from rest_framework import serializers
from shop.models import ShopModel

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShopModel
        fields=('sname','address','email','website','phone')
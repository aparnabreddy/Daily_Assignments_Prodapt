from rest_framework import serializers
from shop.models import Shop

class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('sname','saddres','email','website','phone','username','password')
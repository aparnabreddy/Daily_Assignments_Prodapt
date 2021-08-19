from rest_framework import serializers
from seller.models import Seller

class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sname','add','email','phn','dic','age','ano')
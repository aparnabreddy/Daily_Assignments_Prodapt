from rest_framework import serializers
from Sellers.models import Seller

class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sellername','add','email','phn','district','age','adhar')
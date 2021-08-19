from rest_framework import serializers
from Seller.models import Sellermodel

class SellerSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Sellermodel
        fields=('name','address','email','date','phone','district','adhar')
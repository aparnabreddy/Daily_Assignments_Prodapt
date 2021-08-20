from rest_framework import serializers
from seller.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('seller_name','address','emailID','phno','dob','district','age','aadhar_no')
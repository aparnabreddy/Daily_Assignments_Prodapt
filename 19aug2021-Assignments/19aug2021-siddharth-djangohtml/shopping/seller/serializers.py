from rest_framework import serializers
from seller.models import Sellers
class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Sellers
        fields=("sellername","address","email","phone","dob","district","age","aadharnum")
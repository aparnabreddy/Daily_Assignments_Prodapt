from rest_framework import serializers
from seller.models import Seller

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('selname','seladdress','selemail','selphno','seldob','seldistrict','selage','selaadhar')
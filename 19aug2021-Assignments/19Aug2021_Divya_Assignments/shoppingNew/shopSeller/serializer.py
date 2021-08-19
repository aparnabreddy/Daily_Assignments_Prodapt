from rest_framework import serializers
from shopSeller.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("Seller_Name","Seller_Address","EMail_Id","Phone_Number","Date_of_Birth","District","Age","Adhar_Number")
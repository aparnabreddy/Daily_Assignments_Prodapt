from rest_framework import serializers
from shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("Shop_Name","Address","email_Id","USER_NAME","PASSWORD","Confirm_password","website","phn_no")

from rest_framework import serializers
from Seller.models import Seller
class Sellserializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('selname','seladd','selphone','selemail')

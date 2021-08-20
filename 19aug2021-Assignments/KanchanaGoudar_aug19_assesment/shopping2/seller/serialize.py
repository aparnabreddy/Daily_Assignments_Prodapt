from rest_framework import serializers
from seller.models import Seller

class Sellerserialize(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('Sname','Adress','Email','Phone','Date_of_birth','District','Age','Adharnumber')
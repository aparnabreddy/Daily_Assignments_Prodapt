from rest_framework import serializers
from seller.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sellername','Address','Emailid','MobNum','DOB','Age','AdhaarNum','District')

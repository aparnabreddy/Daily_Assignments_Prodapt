
from rest_framework import serializers
from Product.models import Product
class Productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('prname','prdesc','prprice','prmanfd','prbrand')
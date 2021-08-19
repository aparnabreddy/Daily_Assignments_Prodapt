from rest_framework import serializers
from product.models import product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('pname','pdes','sname','mname','price')
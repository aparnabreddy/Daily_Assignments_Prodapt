from rest_framework import serializers
from Products.models import product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=('productname','productdes','sellername','manufracturename','price')
from rest_framework import serializers
from customerapp.models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("name","email","address","mobilenumber","username","password")
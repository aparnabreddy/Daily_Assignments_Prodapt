from rest_framework import serializers
from customer.models import Customers
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=("name","mname","ntickets","audi","timings","seatnum")
from rest_framework import serializers
from bankapp.models import Bank
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields=('customer_id','customer_name','deposit_amount')
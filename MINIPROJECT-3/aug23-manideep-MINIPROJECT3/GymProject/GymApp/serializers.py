from rest_framework import serializers
from GymApp.models import Customer

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('name','mobilenumber','email','date','adharno','trainingtype')
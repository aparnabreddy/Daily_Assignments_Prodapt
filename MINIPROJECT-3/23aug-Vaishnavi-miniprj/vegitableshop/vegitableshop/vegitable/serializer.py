from django.db import models
from vegitable.models import Vegitablesapp
from rest_framework import serializers
from django.db.models import fields

class VegitablesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vegitablesapp
        fields=('vegitable_code','name','description','packing_date','expiry_date','price')

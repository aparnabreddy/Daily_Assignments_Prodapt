from product.models import product
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from product.models import product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model= product
        fields = ('proname','procode','prodescription','proprice',)


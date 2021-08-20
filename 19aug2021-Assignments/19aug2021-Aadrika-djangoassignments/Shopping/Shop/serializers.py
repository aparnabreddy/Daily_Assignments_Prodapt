from django.db.models import fields
from Shop.models import Shop
from rest_framework import serializers
class Shopserializers(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=('shopname','shopadd','email','phone','username','password')

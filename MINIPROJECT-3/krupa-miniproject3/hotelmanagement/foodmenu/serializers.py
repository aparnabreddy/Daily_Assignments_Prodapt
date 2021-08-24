from rest_framework import serializers
from foodmenu.models import foodmenu

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model=foodmenu
        fields=('breakfast','lunch','dinner','dessert','drinks','chats')
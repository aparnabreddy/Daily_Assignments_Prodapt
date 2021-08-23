from django.db.models import fields
from rest_framework import serializers
from Player_detail.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields = ("Name","Game","Country","Place","Medal")
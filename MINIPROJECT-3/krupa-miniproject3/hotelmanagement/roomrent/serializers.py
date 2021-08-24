from rest_framework import serializers
from roomrent.models import roomrent

class roomrentSerializer(serializers.ModelSerializer):
    class Meta:
        model=roomrent
        fields=('roomclass','nigths','classprice','roomno')
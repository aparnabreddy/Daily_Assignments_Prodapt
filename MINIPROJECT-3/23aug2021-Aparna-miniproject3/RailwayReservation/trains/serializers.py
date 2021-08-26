from django.db.models import fields
from rest_framework import serializers
from trains.models import Trains

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trains
        fields=('trainName','trainNumber','fromStation','toStation','runningDays')
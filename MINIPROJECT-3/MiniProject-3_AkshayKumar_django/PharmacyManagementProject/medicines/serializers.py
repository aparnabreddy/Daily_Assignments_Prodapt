from rest_framework import serializers
from medicines.models import Medicines

class MedicinesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ('rackno','medname','medcat','mfgdate','expdate','cost','stock')
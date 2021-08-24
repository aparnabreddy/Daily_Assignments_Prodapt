from rest_framework import serializers
from Patient.models import Patients

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('pname','padd','pdob','pbg','pcity','pemail','pphone')
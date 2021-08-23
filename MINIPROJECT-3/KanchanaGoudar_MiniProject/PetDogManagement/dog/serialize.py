from rest_framework import serializers
from dog.models import Dog

class DogSerialize(serializers.ModelSerializer):
    class Meta:
        model=Dog
        fields=('Dogid','Dname','Dage','Dprice')
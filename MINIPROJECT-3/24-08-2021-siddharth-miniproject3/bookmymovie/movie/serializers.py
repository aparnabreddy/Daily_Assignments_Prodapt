from rest_framework import serializers
from movie.models import Movies
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields=("city","mname","mduration","mtimings","totalseats","audi")
from rest_framework import serializers
from user.models import User

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('Ucode','Name','Mobileno','Username','Password')
from rest_framework import serializers
from register.models import Registration
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=('name','rollno','college','mailid','examtype','fee','reg_date','reg_close_date')
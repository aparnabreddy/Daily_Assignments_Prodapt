from rest_framework import serializers
from users.models import Users

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name','address','pincode','phone','username','password')
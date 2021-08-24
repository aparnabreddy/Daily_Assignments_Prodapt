from django.db import models
from django.db.models import fields
from rest_framework import serializers
from phonebook.models import PhoneBook

class PhoneBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhoneBook
        fields=('name','number','address','emailid')
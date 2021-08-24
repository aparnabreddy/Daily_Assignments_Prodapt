from django.db.models import fields
from rest_framework import serializers
from country_medal_list.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields = ("Country_name","Gold_medal","Silver_medal","Bronze_medal")
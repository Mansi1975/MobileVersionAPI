from rest_framework import serializers
from .models import MobileVersion

class MobileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileVersion
        fields = '__all__'
        lookup_field = 'version'

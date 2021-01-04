from . models import Register, Login , Data
from rest_framework import serializers

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ['email', 'password', 'name']

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['city', 'code']
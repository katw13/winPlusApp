from rest_framework import serializers
from .models import token

class tokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = token
        fields = '__all__'
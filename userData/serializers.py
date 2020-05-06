from rest_framework import serializers
from .models import CustomerData

class CustomerDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerData
        fields = ('firstName', 'lastName', 'password', 'email', 'phoneNumber')
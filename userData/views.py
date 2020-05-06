from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerData
from .serializers import CustomerDataSerializer

# Create your views here.
class usersInformation(APIView):

    def get(self, request):
        userInfo = CustomerData.objects.all()
        serializer = CustomerDataSerializer(userInfo, many=True)
        return Response(serializer.data)

    def post(self, request):

        # Create an article from the above data
        serializer = CustomerDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


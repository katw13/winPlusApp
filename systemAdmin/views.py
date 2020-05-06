from django.shortcuts import render, redirect
from .models import token, Package
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import tokenSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'systemAdmin/index.html')

def testingTemp(request):
    Dashboard = 'active' 
    context= {
        'Dashboard': Dashboard
    }
    return render(request, 'systemAdmin/dashboard.html', context)

def tokenGeneration(request):
    packages=[500, 1000, 2000, 5000, 10000]
    for package in packages:
        count=1
        while count<=1000:
            tokenPackage = Package.objects.get(cost= package)
            
            savingToken = token(package= tokenPackage, tokenNumber= count, winAmount= 0, winActivation= False, currentInUse= False)
            savingToken1= savingToken.save()

            count +=1

    return render(request, 'systemAdmin/done.html')


class tokenReturn(APIView):

    def get(self, request):
        tokens = token.objects.all()
        serializer = tokenSerializer(tokens, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def loginUser(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            request.session['username']= username
            return redirect('/systemAdmin/testing/')
        else:
            context['error']= 'provide valid credentials'
            return render(request, 'login/login.html' ,context )

def _logout(request):
	logout(request)
	return redirect('/systemAdmin/')
from django.shortcuts import render, HttpResponse
from . models import Register, Login , Data
from . serializers import RegisterSerializer, DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def login(request):
    return HttpResponse("login page")

def register(request):
    Register(name="rahul", email="R@mail.com", password="123456").save()
    return HttpResponse("signup page")

class RegisterView(APIView):
    def get(self, request, format=None):
        allregister = Register.objects.all()
        print(allregister)
        serializer = RegisterSerializer(allregister, many=True)
        print(serializer.data)
        return Response(serializer.data)

def data(request):
    Data(city="indore", code="0731").save()
    return HttpResponse('data page')

class DataView(APIView):
    def get(self, request, format=None):
        alldata = Data.objects.all()
        print(alldata)
        serializer = DataSerializer(alldata, many=True)
        print(serializer.data)
        return Response(serializer.data)

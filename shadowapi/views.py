from django.shortcuts import render, HttpResponse
from . models import Register, Login , Data
from . serializers import RegisterSerializer, DataSerializer
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
import re
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token

def login(request):
    # email = Register.objects.get('email')
    # password = Register.objects.get('password')
    # print(email, passsword)
    return HttpResponse("login page")

def register(request):
    # Register(name="rahul", email="R@mail.com", password=make_password("123456")).save()
    token = Token.objects.create(user=user)
    print(token)
    return HttpResponse("signup page")

class RegisterView(APIView):
    # @authentication_classes([BasicAuthentication])
    # @permission_classes([IsAuthenticated])
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
       
        allregister = Register.objects.all()
        # authentication_classes=[BasicAuthentication]
        # permission_classes=[IsAuthenticated]
        # print(allregister)
        serializer = RegisterSerializer(allregister, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        email = request.POST['email']
        name = request.POST['name']
        password = make_password(request.POST.get('password'))
        print(password)

        # if len(password) < 8:
        #     return Response({"status": '201', "error": "password should be grater than 8 chars"})
        # else:
        #     Register(name=name, email=email, password=password).save()
        #     serializer = {"name": name, "password":password, "email":email}
        #     return Response(serializer)

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex,email)):
            Register(name=name, email=email, password=password).save()
            serializer = {"name": name, "password":password, "email":email}
            return Response(serializer)
        else:
            return Response({"status": '201', "error": "Email is Invalid"})

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

class LoginView(APIView):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == None or password == None:
            return Response({'error' : 'fill all neccessary fields'})
        
        result = Register.objects.filter(email=email).first()
        print(result)
        print(password)
        print(result.password)
        print(check_password(str(result.password)), str(password))
        if check_password(result.password, str(password)):
            return Response("ok")
        else:
            return Response('wrong password')
        
        # if result:
        #     return Response({'response' : 'email exist'})
        # else: 
        #     return Response({'response' : 'not Found'})


        

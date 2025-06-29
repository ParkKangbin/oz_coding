
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyinfoUserSerializer
from django.contrib.auth.password_validation import validate_password

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Users(APIView):
    def post(self, request):

        password = request.data.get('password')
        serializer = MyinfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()

            serializer = MyinfoUserSerializer(user)
            return Response(serializer.data,status=201)
        else:
            raise ParseError(serializer.errors)
        
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        serializer = MyinfoUserSerializer(user)

        return Response(serializer.data)
    
    def put(self,request):
        user = request.user

        serializer = MyinfoUserSerializer(user,data = request.data,partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyinfoUserSerializer(user)

            return Response(serializer.data, status = 201)
        else:
            return Response(serializer.errors,status = 401)
        

from django.contrib.auth import authenticate,login
from rest_framework import status
# api/v1/users/login        
class Login(APIView):
    def post(self,requset):
        username = requset.data.get('username')
        password = requset.data.get('password')

        if not username or not password:
            raise ParseError()
        
        user = authenticate(requset,username = username, password = password)

        if user:
            login(requset,user)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
from django.contrib.auth import logout

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("header :",request.headers)

        logout(request)

        return Response(status=status.HTTP_200_OK)
    
import jwt
from django.conf import settings

class JWTLogin(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("paasword")

        if not username or not password:
            raise ParseError
        
        user = authenticate(request, username=username,password=password)

        if user:
            payload = {"id":user.id,"username":username}

            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256"
            )

            return Response({"token":token})
        
from config.authentication import JWTAuthentication

class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username
        })
    
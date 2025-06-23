
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyinfoUserSerializer
from django.contrib.auth.password_validation import validate_password
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
        



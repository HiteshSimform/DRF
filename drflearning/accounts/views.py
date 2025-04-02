from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CustomUserRegistrationView(APIView):
    def post(self, request):
        print("Register")
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class CustomUserRegistrationView(APIView):
#     def post(self, request):
#         print("Register")
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserLoginView(ObtainAuthToken,APIView):
    def post(self, request, *args, **kwargs):
        print("In Custom user")
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()
                token  = Token.objects.create(user=user)
            return Response({'token':token.key, 'username':user.username, 'role':user.role})
        else:
            return Response({'message':'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomUserLogoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers)
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'details':'Successfully logged out.'})
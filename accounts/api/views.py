from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import UserLoginSerializer, UserRegistrationSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserRegistrationView(APIView):   #handle user registration via post request
    authentication_classes = []    #disables authentication for registration
    permission_classes = [AllowAny]  # allows any user to register
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  #generates token for the registerd user
            return Response({"token": token.key, "user_id": user.id}, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationTemplateView(TemplateView):
    template_name = "accounts/register.html"

class UserLoginTemplateView(TemplateView):
    template_name = "accounts/login.html"


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password = serializer.validated_data['password'])
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key, "user_id":user.id}, status=status.HTTP_201_CREATED)
            return Response({"errors": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  #ensures only authenticated users can access this view

    def get(self, request):   #retrieves authenticated user profile
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):   #this method allows logged in user to update their profile
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)   #partial updates are allowed
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


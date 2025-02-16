"""
This module provides API endpoints for user authentication, including signup and login.
It utilizes Django's authentication framework and token-based authentication.
"""

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer

class SignupView(APIView):
    """
    API endpoint for user registration.
    
    Request:
    - `username`: Required string for the new user's username.
    - `password`: Required string for the new user's password.
    
    Response:
    - Returns an authentication token and username upon successful signup.
    - Returns validation errors if the request is invalid.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API endpoint for user login.
    
    Request:
    - `username`: Required string for authentication.
    - `password`: Required string for authentication.
    
    Response:
    - Returns an authentication token and username if login is successful.
    - Returns an error message if authentication fails.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

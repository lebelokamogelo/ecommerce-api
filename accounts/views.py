from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate, login, logout
import requests
import json


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(**request.data)

    if user:
        return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user:
        login(request, user)

        token = requests.post('http://127.0.0.1:8000/auth/token/', json=request.data)

        if token.status_code == 200:
            return Response({"token": token.json().get('access')}, status=status.HTTP_200_OK)
        else:
             return Response({'error': 'Token retrieval failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'error': 'Incorrect email or password.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signout(request):
    logout(request)
    # TODO: Add the refresh token to the blacklist to prevent the user use it again.
    return Response({'success': True}, status=status.HTTP_200_OK)
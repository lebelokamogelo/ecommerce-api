from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate, login, logout
import requests

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(**request.data)
    if user:
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin(request):
    user = authenticate(request, **request.data)
    token = requests.post('http://127.0.0.1:8000/auth/token/', json={**request.data})

    if user and token:
        login(request, user)
        return Response({"token": token}, status=status.HTTP_200_OK)
    return Response({'error': 'Incorrect email or password.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signout(request):
    logout(request)
    # TODO: Add the refresh token to the blacklist to prevent the user use it again.
    return Response({'success': True}, status=status.HTTP_200_OK)
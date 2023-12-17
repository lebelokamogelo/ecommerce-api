from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    endpoints = [
        '/api/v1/products/',
        '/api/v1/products/<str:pk>/',
        '/api/v1/products/?category=name',
        '/api/v1/category/',
        '/api/v1/category/<str:name>/',
        '/api/v1/reviews/<str:pk>/'
    ]

    return Response(endpoints, status=status.HTTP_200_OK)
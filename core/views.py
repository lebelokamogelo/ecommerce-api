from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    endpoints = [
        '/api/v1/products/',
        '/api/v1/products/<str:pk>/',
        '/api/v1/products/<str:pk>/reviews/',
        'api/v1/reviews/<str:pk>/',
        '/api/v1/products/?category=?',
        '/api/v1/products/?page=?&page_size=?',
        '/api/v1/category/',
        '/api/v1/category/<str:name>/',
        '/api/v1/cart/',
        '/api/v1/cart/delete/<str:pk>/',
        '/api/v1/cart/delete/',
    ]

    return Response(endpoints, status=status.HTTP_200_OK)

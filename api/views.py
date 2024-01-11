from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Categorie, Cart, CartItem
from .pagination import PageNumberPagination
from .permissions import IsAdmin, IsAdminOrManager, IsCustomer
from .serializers import (CategorySerializer, ProductSerializer,
                          CartSerializer, ReviewSerializer)


class Products(generics.GenericAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self, *args, **kwargs):
        if self.request.method == 'POST':
            return [IsAdminOrManager()]
        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        name = self.request.GET.get('category') or None
        if name:
            category = get_object_or_404(Categorie, name__icontains=name)
            return self.queryset.filter(category=category)
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid():
            category = self.request.data.get('category')
            instance = get_object_or_404(Categorie, name=category)
            serializer.save(category=instance)
            return Response(status=status.HTTP_201_CREATED)


class ProductsReadUpdateDelete(generics.GenericAPIView,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [IsAdminOrManager()]
        elif self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsAuthenticatedOrReadOnly()]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductReview(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ReviewSerializer
    lookup_field = 'pk'
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsCustomer()]
        return [IsAuthenticatedOrReadOnly()]

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))

    def get_queryset(self):
        return self.get_object().review_set.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class Category(generics.GenericAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrManager]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class CategoryReadUpdate(generics.GenericAPIView,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    permission_classes = [IsAdminOrManager]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart_related_items = request.user.cart.cartitem_set.all()
        serializer = CartSerializer(cart_related_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=2)
            cart, created = Cart.objects.get_or_create(user=request.user)
            CartItem.objects.create(cart=cart, product=product, quantity=1)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class DeleteCartItems(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        try:
            cart.cartitem_set.all().delete()
        except Exception as e:
            return Response(str(e), status=status.HTTP_304_NOT_MODIFIED)

        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        try:
            cart.cartitem_set.get(pk=kwargs.get('pk')).delete()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

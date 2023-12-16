from rest_framework import generics, mixins, status
from products.models import Product, Categorie
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class Products(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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


class ProductsRUD(generics.GenericAPIView, mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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


class Category(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryRU(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CategoryProducts(APIView):
    def get(self, request, name, *args, **kwargs):
        category = get_object_or_404(Categorie, name=name)
        data = category.product_set.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

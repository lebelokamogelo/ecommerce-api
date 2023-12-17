from rest_framework import serializers
from products.models import *
from .validators import category_name
from accounts.models import User


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[category_name])
    class Meta:
        model = Categorie
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'description',
            'price',
            'quantity',
            'category',
        ]


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'username'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = [
            'pk',
            'user',
            'rating',
            'comment',
            'created_at',
            'updated_at',
            ]

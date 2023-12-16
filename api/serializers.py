from rest_framework import serializers
from products.models import *
from .validators import category_name

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

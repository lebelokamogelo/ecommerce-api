from products.models import Categorie
from rest_framework import serializers

def category_name(value):
    category = Categorie.objects.get(name__icontains=value)
    if category:
        raise serializers.ValidationError('This field must be unique.')
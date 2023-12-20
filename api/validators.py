from products.models import Categorie
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

def category_name(value):
    try:
        category = Categorie.objects.get(name__icontains=value)
        raise serializers.ValidationError('This field must be unique.')
    except ObjectDoesNotExist:
        # If no category is found, the name is unique, so return the value
        return value

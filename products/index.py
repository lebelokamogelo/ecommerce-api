from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product


@register(Product)
class ProductModelIndex(AlgoliaIndex):
    fields = ('name', 'description', 'price', 'quantity', 'category')
    settings = {'searchableAttributes': ['name', 'description', 'category']}
    index_name = 'ecommerce'

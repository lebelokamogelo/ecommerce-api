from algoliasearch_django import algolia_engine


def get_index():
    index = algolia_engine.client.init_index('ecommerce')
    return index


def search(query):
    index = get_index()
    return index.search(query)

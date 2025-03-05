from django_elasticsearch_dsl import document, fields
from django_elasticsearch_dsl.registries import registry
from product.models import Product

@registry.register_document
class ProductDocument(document):
    class Index:
        name = 'products'
    class Django:
        model = Product
        fields = ['name', 'description', 'price', 'category']
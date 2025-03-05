from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from product.models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
    class Django:
        model = Product
        fields = ['name', 'description', 'price']
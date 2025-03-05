from django.apps import AppConfig
from django.db import connections


class SearchProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_products'

    def ready(self):
        connections.create_connection(alias='default')

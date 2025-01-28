from django.db import models
from search_products.models import Category

# Create your models here.

#model class for product
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= "products")
    description = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(blank=False, null=False, default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="static/product_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.created_at}"

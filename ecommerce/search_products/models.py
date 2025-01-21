from django.db import models

# Create your models here.

#model class for category
class Category(models.Model):   #inherits Model
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null= True)
    create_date = models.DateTimeField(auto_now_add=True)    #automatically sets the current time

    def __str__(self):
        return self.name

#model class for product
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= "products")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.category} {self.price} {self.created_at}"
    

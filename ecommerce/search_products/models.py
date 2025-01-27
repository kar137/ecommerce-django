from django.db import models

# Create your models here.

#model class for category
class Category(models.Model):   #inherits Model
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null= True)
    create_date = models.DateTimeField(auto_now_add=True)    #automatically sets the current time

    def __str__(self):
        return self.name



    

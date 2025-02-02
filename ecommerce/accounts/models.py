from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to="profile_pics/", blank= True, null= True)
    address = models.CharField(max_length=255, blank= True, null= True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoids conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoids conflict
        blank=True
    )

    def __str__(self):
        return self.username
    

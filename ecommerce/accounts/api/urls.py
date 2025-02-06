from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserRegistrationTemplateView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register-api'),
    path('api/login/', UserLoginView.as_view(), name='login-api'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/', UserRegistrationTemplateView.as_view(), name='register'),
]
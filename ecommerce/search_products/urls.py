from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.HomeView.as_view() ),
    path('product-form/', views.ProductView.as_view(), name= "product-form")
]

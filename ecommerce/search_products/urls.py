from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.HomeView.as_view(), name= "home" ),
    path('category-products/<int:pk>', views.CategoryProductsView.as_view(), name= "category-products" ),
     path('shop-now', views.ShopNowView.as_view(), name= "shop-now" )
]

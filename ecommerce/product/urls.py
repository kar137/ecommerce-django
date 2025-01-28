from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 

urlpatterns = [
    path('product-form', views.ProductView.as_view(), name= "product-form"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name= "product-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
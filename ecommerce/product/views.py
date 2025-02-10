from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.base import TemplateView
from .forms import ProductForm
from .models import Product

# Create your views here.

#view for product details
class ProductView(FormView, ListView):
    template_name = "product/product_form.html"
    form_class = ProductForm
    success_url = "product-detail"  # Redirect after successful form submission
    context_object_name = "products"

    def get_queryset(self):
        # Customize the queryset for featured products
<<<<<<< HEAD
        return Product.objects.order_by("created_at")[:5]   #orders the products in descending order and selects the top five
=======
        return Product.objects.order_by("created_at")[:5] # Orders the products in descending order and use slicing technique
>>>>>>> 6347d0706809b0e25c16c4e36480b8190d7048f7

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Add both the form and the featured products to the context
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Add the form to the context
        return context
    
class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product
    context_object_name = "product"


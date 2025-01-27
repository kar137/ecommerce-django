from django.shortcuts import render
from django.views.generic import FormView, ListView
from search_products.forms import ProductForm
from search_products.models import Product

# Create your views here.

#view for product details
class ProductView(FormView, ListView):
    template_name = "product/product_form.html"
    form_class = ProductForm
    success_url = "home"  # Redirect after successful form submission
    context_object_name = "featured_products"

    def get_queryset(self):
        # Customize the queryset for featured products
        return Product.objects.filter(is_featured=True)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Add both the form and the featured products to the context
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Add the form to the context
        return context

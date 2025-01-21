from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from .models import Category, Product
from .forms import ProductForm

# Create your views here.

#renders home view
class HomeView(ListView):
    template_name = "search_products/home.html"
    model = Category
    context_object_name = "categories"
    

#view for product details
class ProductView(FormView, ListView):
    template_name = "search_products/product_form.html"
    form_class = ProductForm
    success_url = "/products/"  # Redirect after successful form submission
    context_object_name = "featured_products"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)





from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from product.models import Product
from .models import Category

# Create your views here.

#renders home view
class HomeView(ListView):
    template_name = "search_products/home.html"
    model = Category
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_products"] = Product.objects.filter(is_featured = True)
        return context
    

class CategoryProductsView(DetailView):
    template_name = "search_products/category_products.html"
    model = Category
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id = self.kwargs['pk'])  #helps to retrieve pk from the url
        context["products"] = Product.objects.filter(category = category)
        return context
    
    






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
    






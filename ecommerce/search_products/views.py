from django.shortcuts import render
from django.views.generic.base import TemplateView
from django import views

# Create your views here.

class HomeView(TemplateView):
    template_name = "search_products/home.html"



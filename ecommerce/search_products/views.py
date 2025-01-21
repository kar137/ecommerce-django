from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Category, Product
from .forms import ProductForm

# Create your views here.

#renders home view
class HomeView(ListView):
    template_name = "search_products/home.html"
    model = Category
    context_object_name = "categories"
    

#view for product details
class ProductView(ListView):
    template_name = "search_products/product_form.html"
    model = Product
    
    #worksout with the productform
    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():   #validates the form
            form.save()
            products = Product.objects.all()   #access all the products saved to the database
            return HttpResponseRedirect("search_products/home.html", {
                "featured_products": products,
            })
        
        return render(request, "search_products/product_form.html", {
            "form": form,
        })
    





from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from elasticsearch_dsl import Q
from product.models import Product
from .models import Category
from search_products.documents import ProductDocument
# Create your views here.


class SearchView(View):
    template_name = 'search_products.html'
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        results = []

        if query:
            q = Q('multi_match', query=query, fiels=['name', 'description'])
            results = ProductDocument.search.query(Q)
        return render(request, self.template_name, {'results': results, 'query': query})

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

class ShopNowView(ListView):
    template_name = "search_products/shopnow.html"
    model = Product
    context_object_name = "products"   

    
    






from .models import Category

def categories_processor(request):  #returns the context for templates outside the app
    return {"categories": Category.objects.all()}
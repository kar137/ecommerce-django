from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product 
        fields = "__all__"
        exclude = ["created_at",]   #excludes the field given

    #adds tailwindcss styling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'border p-2 w-full rounded-md'})
        self.fields['category'].widget.attrs.update({'class': 'border p-2 w-full rounded-md'})
        self.fields['image'].widget.attrs.update({'class': 'border p-2 w-full rounded-md'})
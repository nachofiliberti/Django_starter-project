from django import forms
from .models import Category, Product, Supplier, ProductReview, PriceHistory, ProductImage

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'category': forms.Select(attrs={'class': 'form-control custom-class'}),
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'description': forms.Textarea(attrs={'class': 'form-control custom-class'}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'contact': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'phone': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'address': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            "product",
            "author",
            "text",
            "rating",
        ]
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-class'}),
            'author': forms.Select(attrs={'class': 'form-control custom-class'}),
            'text': forms.Textarea(attrs={'class': 'form-control custom-class'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }

class PriceHistoryForm(forms.ModelForm):
    class Meta:
        model = PriceHistory
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-class'}),
            'price': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'date': forms.DateInput(attrs={'class': 'form-control custom-class'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'product',
            'image',
            'description',
        ]
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control custom-class'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-class'}),
            'description': forms.Textarea(attrs={'class': 'form-control custom-class'}),
        }

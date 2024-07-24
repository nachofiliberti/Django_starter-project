from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from product.forms import ProductForm
from product.models import Category, Product, ProductImage
from product.repositories.product import ProductRepository
from product.repositories.category import CategoryRepository

repo_category = CategoryRepository()
repo = ProductRepository()

class ProductListView(View):
    def get(self, request):
        productos = repo.get_all()
        return render(
            request,
            'products/list.html',
            dict(
                products=productos
            )
        )

class ProductDetailView(View):
    def get(self, request, id):
        producto = get_object_or_404(Product, id=id)
        imagen = ProductImage.objects.filter(product=producto).first()
        return render(
            request,
            'products/detail.html',
            dict(product=producto,
                imagen=imagen
            )
        )


class ProductDeleteView(View):
    def get(self, request, id):
        producto = get_object_or_404(Product, id=id)
        repo.delete(producto=producto)
        return redirect('product_list')


class ProductUpdateView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        categorias = repo_category.get_all()
        form = ProductForm(instance=product)
        return render(
            request,
            'products/update.html',
            dict(
                categories=categorias,
                form=form
            )
        )
    
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id=product.id)
        categorias = repo_category.get_all()
        return render(
            request,
            'products/update.html',
            dict(
                categories=categorias,
                form=form
            )
        )


class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(
            request,
            'products/create.html',
            dict(
                form=form
            )
        )
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre=form.cleaned_data['name'],
                precio=form.cleaned_data['price'],
                descripcion=form.cleaned_data['description'],
                cantidades=form.cleaned_data['stock'],
                categoria=form.cleaned_data['category']
            )
            return redirect('product_detail', producto_nuevo.id)
        return render(
            request,
            'products/create.html',
            dict(
                form=form
            )
        )

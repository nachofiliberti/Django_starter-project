from django.shortcuts import get_object_or_404, render, redirect
from django.views import View

from product.repositories.category import CategoryRepository
from product.repositories.product import ProductRepository
from django.contrib.auth.decorators import login_required
from product.forms import CategoryForm
from django.utils.decorators import method_decorator


class CategoryListView(View):
    def get(self, request):
        category_repository = CategoryRepository()
        categorias = category_repository.get_all()
        return render(
            request,
            'categories/list.html',
            dict(
                categories=categorias
            )
        )

class CategoryDetailView(View):
    def get(self, request, id: int):
        category_repository = CategoryRepository()
        product_repository = ProductRepository()
        categoria = category_repository.get_by_id(id)
        productos = product_repository.filter_by_category(categoria)
        return render(
            request,
            'categories/detail.html',
            dict(
                category=categoria,
                products=productos
            )
        )


class CategoryDeleteView(View):
    def get(self, request, id: int):
        category_repository = CategoryRepository()
        categoria = category_repository.get_by_id(id)
        category_repository.delete(categoria)
        return redirect('category_list')



class CategoryUpdateView(View):
    def get(self, request, id: int):
        category_repository = CategoryRepository()
        categoria = category_repository.get_by_id(id)
        form = CategoryForm(instance=categoria)
        return render(
            request,
            'categories/update.html',
            dict(
                form=form
            )
        )
    
    def post(self, request, id: int):
        category_repository = CategoryRepository()
        categoria = category_repository.get_by_id(id)
        form = CategoryForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        return render(
            request,
            'categories/update.html',
            dict(
                form=form
            )
        )
    

class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        return render(
            request,
            'categories/create.html',
            dict(
                form=form
            )
        )
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        return render(
            request,
            'categories/create.html',
            dict(
                form=form
            )
        )
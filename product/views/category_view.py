from django.shortcuts import render, redirect

from product.repositories.category import CategoryRepository
from product.repositories.product import ProductRepository

def category_list(request):
    category_repository = CategoryRepository ()
    categorias = category_repository.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )

def category_detail(request, id: int):
    category_repository = CategoryRepository ()
    product_repository = ProductRepository()
    categoria = category_repository.get_by_id(id)
    productos = product_repository.filter_by_category(categoria)
    return render(
        request,
        'categories/detail.html',
        dict(category=categoria,
            products=productos
        )
    )

def category_delete(request, id: int):
    category_repository = CategoryRepository ()
    categoria = category_repository.get_by_id(id)
    category_repository.delete(categoria)
    return redirect ('category_list')



def category_update(request, id: int):
    category_repository = CategoryRepository ()
    categoria = category_repository.get_by_id(id)
    if request.method == 'POST':
        nombre = request.POST.get('name')


        category_repository.update(
            category=categoria,
            nombre=nombre
        )


        return redirect('category_list')
    return render(
        request,
        'categories/update.html',
        dict(
            category=categoria,
        )
    )

def category_create(request):
    category_repository = CategoryRepository ()
    if request.method == 'POST':
        nombre = request.POST.get('name')
        category_repository.create(
            nombre=nombre,
        )

        return redirect('category_list')
    return render (
        request, 
        'categories/create.html',
    )
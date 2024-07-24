from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from product.models import Supplier
from product.repositories.supplier import SupplierRepository
from product.forms import SupplierForm

repo = SupplierRepository()

class SupplierListView(View):
    def get(self, request):
        suppliers = repo.get_all()
        return render(
            request,
            'supplier/list.html',
            dict(
                suppliers=suppliers
            )
        )

class SupplierDetailView(View):
    def get(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        return render(
            request,
            'supplier/detail.html',
            dict(
                supplier=supplier
            )
        )


class SupplierCreateView(View):
    def get(self, request):
        form = SupplierForm()
        return render(
            request,
            'supplier/create.html',
            dict(
                form=form
            )
        )

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = repo.create(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            return redirect('supplier_detail', supplier.id)
        return render(
            request,
            'supplier/create.html',
            dict(
                form=form
            )
        )


class SupplierUpdateView(View):
    def get(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        form = SupplierForm(instance=supplier)
        return render(
            request,
            'supplier/update.html',
            dict(
                form=form
            )
        )

    def post(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_detail', supplier.id)
        return render(
            request,
            'supplier/update.html',
            dict(
                form=form
            )
        )


class SupplierDeleteView(View):
    def get(self, request, id):
        supplier = get_object_or_404(Supplier, id=id)
        repo.delete(supplier)
        return redirect('supplier_list')
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.decorators import login_required

from product.views.product_view import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

from product.views.category_view import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
) 

from product.views.supplier_view import (
    SupplierListView,
    SupplierDetailView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
)

from product.views.product_review_view import (
    ProductReviewView,
    ProductReviewCreateView,
    ProductReviewDetailView,
    ProductReviewDeleteView,
    ProductReviewUpdateView,
)

from product.views.product_image_view import ProductImageView 

urlpatterns = [

    # Productos usando vistas basadas en clases
    path('', login_required(ProductListView.as_view(), login_url='login'), name='product_list'),
    path('create/', login_required(ProductCreateView.as_view(), login_url='login'), name='product_create'),
    path('<int:id>/', login_required(ProductDetailView.as_view(), login_url='login'), name='product_detail'),
    path('<int:id>/update/', login_required(ProductUpdateView.as_view(), login_url='login'), name='product_update'),
    path('<int:id>/delete/', login_required(ProductDeleteView.as_view(), login_url='login'), name='product_delete'),

    # Categorías usando vistas basadas en clases
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:id>/', login_required(CategoryDetailView.as_view(), login_url='login'), name='category_detail'),
    path('category/create/', login_required(CategoryCreateView.as_view(), login_url='login'), name='category_create'),
    path('category/<int:id>/update/', login_required(CategoryUpdateView.as_view(), login_url='login'), name='category_update'),
    path('category/<int:id>/delete/', login_required(CategoryDeleteView.as_view(), login_url='login'), name='category_delete'),

    # Proveedores usando vistas basadas en clases
    path('supplier/', login_required(SupplierListView.as_view(), login_url='login'), name='supplier_list'),
    path('supplier/create/', login_required(SupplierCreateView.as_view(), login_url='login'), name='supplier_create'),
    path('supplier/<int:id>/', login_required(SupplierDetailView.as_view(), login_url='login'), name='supplier_detail'),
    path('supplier/<int:id>/delete/', login_required(SupplierDeleteView.as_view(), login_url='login'), name='supplier_delete'),
    path('supplier/<int:id>/update/', login_required(SupplierUpdateView.as_view(), login_url='login'), name='supplier_update'),

    # Reseñas usando vistas basadas en clases
    path('reviews/', ProductReviewView.as_view(), name='review_list'),
    path('reviews/create/', login_required(ProductReviewCreateView.as_view(), login_url='login'), name='review_create'),
    path('reviews/<int:id>/detail/', ProductReviewDetailView.as_view(), name='review_detail'),
    path('reviews/<int:id>/delete/', login_required(ProductReviewDeleteView.as_view(), login_url='login'), name='review_delete'),
    path('reviews/<int:id>/update/', login_required(ProductReviewUpdateView.as_view(), login_url='login'), name='review_update'),
    path('product_images/', login_required(ProductImageView.as_view(), login_url='login'), name='product_images'),
]
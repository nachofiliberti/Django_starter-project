from django.contrib import admin
from django.urls import path, include

from product.views.index_view import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('products/', include("product.urls")),
]
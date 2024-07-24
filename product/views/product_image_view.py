from django.shortcuts import redirect, render, get_list_or_404
from django.views import View

from product.forms import ProductImageForm
from product.models import ProductImage

class ProductImageView(View):
    def get(self, request):
        images = ProductImage.objects.all()
        return render(
            request,
            'product_images/list.html',
            dict(
                images = images
            )
        )
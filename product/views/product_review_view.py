from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from django.shortcuts import render, redirect

from product.models import ProductReview 
from product.repositories.product import ProductRepository
from product.repositories.product_reviews import ProductReviewRepository
from product.forms import ProductReviewForm

class ProductReviewView(View):
    def get(self, request,):
        repo = ProductReviewRepository()
        reviews = repo.get_all()

        #si el usuario esta auntenticado y no es  staff solo puede ver las opiniones propias y no de todos
        if request.user.is_authenticated and not request.user.is_staff:
            reviews = reviews.filter(author=request.user)

        return render(
            request,
            'product_reviews/list.html',
            dict(
                reviews=reviews,
            )
        )
    

class ProductReviewCreateView(View):
    def get(self, request,):
        form = ProductReviewForm()
        return render(request,
                    'product_reviews/create.html',
                    dict(
                        form=form)
                    )

    def post(self, request):
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            repo = ProductReviewRepository()
            repo.create(
                product_id=form.cleaned_data['product'].id,
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text'],
                rating=form.cleaned_data['rating'],
            )
            return redirect('review_list')
        return render(request,
                    'product_reviews/create.html',
                    dict(
                        form=form,
                    )
                )

class ProductReviewDetailView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        return render(
            request,
            'product_reviews/detail.html',
            dict(
                review=review
            )
        )

class ProductReviewDeleteView(View):
    def get(self, request, id):
        repo = ProductReviewRepository()
        review = repo.get_by_id(id=id)
        repo.delete(review=review)
        return redirect('review_list')

class ProductReviewUpdateView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(instance=review)
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )
    
    def post(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )
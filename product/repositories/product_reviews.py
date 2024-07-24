from typing import (
    List,
    Optional,
)

from product.models import (
    ProductReview,
)

from django.contrib.auth.models import User

from product.repositories.product import ProductRepository

class ProductReviewRepository:

    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def get_by_id(self, id) -> ProductReview:
        return ProductReview.objects.get(id = id)
    
    def create(
        self,
        product_id: int,
        author: User,
        text: str,
        rating: int
    ) -> ProductReview:
        product_repo = ProductRepository()
        product = product_repo.get_by_id(product_id)
        review = ProductReview.objects.create(
            product=product,
            author=author,
            text=text,
            rating=rating,
        )
        return review
    
    def delete(self, review: ProductReview):
            review.delete()
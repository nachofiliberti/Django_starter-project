from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
    )
    stock = models.IntegerField(default=0)

    def __str__(self):
        return  self.name

    @admin.display(description="Rango de Precio")
    def rango_precios(self):
        if self.price > 1000000:
            return "ALTO"
        if 500000< self.price < 1000000:
            return "MEDIO"
        return "BAJO"


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()

    def __str__(self):
        return f'Review by {self.author.username} for {self.product.name}'
    

class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='price_history'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.price} on {self.date}'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.product.name}'


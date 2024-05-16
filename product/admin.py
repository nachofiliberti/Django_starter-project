from django.contrib import admin
from django.utils.html import format_html

from product.models import (
    Category,
    Product,
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name', 'price')
    search_fields = ('price', 'name', 'category__name',)
    list_filter = ('category', 'name',)
    #list_editable = ('price',)
    #exclude = ('price',)
    empty_value_display = "No hay datos para este campo"
    readonly_fields =  ("name",)
    #list_display_links = ("price","name",)

    list_display = (
        'name',
        'price',
        'rango_precios',
        'description',
        'category',
        'get_stock',
        'valor_total',
    )

    fieldsets = [
        (
            "Info del Producto",
            {
                "fields" : ["name", "price"],
            }
        ),
        (
            "Info Extra",
            {
                "classes":["collapse"],
                "fields" : ["stock", "description"]
            }
        )
    ]


    def valor_total(self, obj):
        return obj.stock * obj.price
    
    def get_stock(self, obj):
        codigo = "#FF0000"
        if obj.stock >= 500:
            codigo = "#008000"
        if 500 > obj.stock > 10:
            codigo = "#FFD300"
        return format_html(
            '<span style="color:{};">{}</span>',
            codigo, obj.stock
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

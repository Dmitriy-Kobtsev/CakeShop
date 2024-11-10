from django.contrib import admin

from bakery.models import Products, Category

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'price', 'weight', 'description', 'content', 'nutritional_value', 'product_category')
    list_filter = ('product_category', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')

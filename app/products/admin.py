from django.contrib import admin

from products.models import Product, ProductImage, Genre


class ProductImageInline(admin.TabularInline):
    model = ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]
    filter_horizontal = ('genres',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
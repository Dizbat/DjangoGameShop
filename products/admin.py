from django.contrib import admin
from .models import *


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discont', 'is_active')
    inlines = [ProductImagesInline]
    list_filter = ('created', 'updated')

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'type', 'is_active')

    class Meta:
        model = ProductImages


admin.site.register(ProductImages, ProductImagesAdmin)

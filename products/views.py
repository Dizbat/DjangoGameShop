from django.shortcuts import render
from .models import ProductImages, Product


def home(request):
    product_images = ProductImages.objects.filter(is_active=True, type='card')
    return render(request, 'product/home.html', locals())


def product(request, product_id):
    game = Product.objects.get(id=product_id)
    main_image = ProductImages.objects.get(product=Product.objects.get(id=product_id), is_active=True, type='main')
    screen = ProductImages.objects.filter(product=Product.objects.get(id=product_id), is_active=True, type='screenshot')
    return render(request, 'product/buy_page.html', locals())





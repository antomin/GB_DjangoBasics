from datetime import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket

from .models import Contact, Product, ProductCategory


def main(request):
    title = "главная"
    products = Product.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}

    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user) 

    if pk is not None:
        if pk == 0:
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'media_url': settings.MEDIA_URL,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
        'basket': basket
    }

    if pk:
        print(pk)

    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "контакты"
    visit_date = datetime.now()
    contacts = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "contacts": contacts}

    return render(request, "mainapp/contact.html", content)

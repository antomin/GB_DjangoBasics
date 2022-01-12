from datetime import datetime

from django.conf import settings
from django.shortcuts import render

from .models import Contact, Product, ProductCategory


def main(request):
    title = "главная"
    products = Product.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}

    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,
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

from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"  # Объясните, пожалуйста, что это за переменная и зачем она нужна

urlpatterns = [
    path("", mainapp.products, name="index"),
    path("category/<int:pk>/", mainapp.products, name="category")
]

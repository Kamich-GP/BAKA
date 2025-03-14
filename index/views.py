from django.shortcuts import render
from .models import Category, Product


# Create your views here.
# Главная страница
def home_page(request):
    # Вывод всех данных из БД
    categories = Category.objects.all()
    products = Product.objects.all()

    # Передаем данные на фронт
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'home.html', context)


# Вывод товаров по категории
def category_page(request, pk):
    # Достаем данные из БД
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)

    # Передаем данные на фронт
    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category.html', context)

# Вывод определенного товара
def product_page(request, pk):
    # Достаем данные из БД
    product = Product.objects.get(id=pk)

    # Отправляем данные на фронт
    context = {
        'product': product
    }

    return render(request, 'product.html', context)

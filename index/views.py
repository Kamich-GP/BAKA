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

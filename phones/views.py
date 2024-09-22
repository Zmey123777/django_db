from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    # Получаем параметр сортировки из запроса
    sort = request.GET.get('sort')
    
    # Извлекаем все телефоны из базы данных
    phones = Phone.objects.all()

    # Проверяем, по какому параметру нужно отсортировать
    if sort == 'name':
        phones = phones.order_by('name')  # Сортировка по имени
    elif sort == 'min_price':
        phones = phones.order_by('price')  # Сортировка по возрастанию цены
    elif sort == 'max_price':
        phones = phones.order_by('-price')  # Сортировка по убыванию цены

    context = {
        'phones': phones
    }
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

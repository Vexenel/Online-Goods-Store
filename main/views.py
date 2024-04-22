from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first

def index(request):
    context: dict = {
        'title': 'Home - Главная' ,
        'content': 'Интернет-магазина бытовой техники'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Home - О нас' ,
        'content': 'О нас',
        'text_on_page': "Наш магазин супер пупер,гипер крутой и в нем можно найти все что угодно вашей душе"
    }

    return render(request, 'main/about.html', context)   

def deli(request):
    context: dict = {
        'title': 'Home - Доставка' ,
        'content': 'Доставка и оплата',
        'text_on_page': "Здесь укаывается ваш адрес и сумма вашего заказа"
    }

    return render(request, 'main/deli.html', context)   

def cont(request):
    context: dict = {
        'title': 'Home - Контактная информация' ,
        'content': 'Контактная информация',
        'text_on_page': "Наши адреса и телефонные номера"
    }

    return render(request, 'main/cont.html', context)  
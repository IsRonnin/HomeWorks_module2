from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .myClass import *
import random


products_list = filled()
products_list.append(None)


def hello(request: HttpRequest):
    obj = Product("Royal Canin", "Сухой корм", "600 ₽", "Коты", '1000 г') # Условный обьект.
    my_info = f'Я {"Артём Ващенко"} мне {"15"} и я люблю кодить! Вот вам случайное число! <{random.randint(-1000, 1000)}> <br>' + str(obj)
    return HttpResponse(my_info, status=200)

def start_page(request: HttpRequest):
    return HttpResponse('<a href="hello/">Дз_1</a><br><a href="products/">Список товаров</a> <br><br>' + 
                        '<br>'.join(f'<a href="products/product/{indx}">Продукт: {indx}</a><br>'.format(products_list[indx]) if products_list[indx] != None 
                                    else f'<a href="products/product/{indx}">Продукт: None</a><br>'.format(products_list[indx]) 
                                    for indx in range(len(products_list))), status=200)


@csrf_exempt
def products(request:HttpRequest):
    if request.method == 'GET':
        print('<br>'.join(str(product) for product in products_list))
        return HttpResponse('<br>'.join(str(product) for product in products_list), status=200)
    
    if request.method == 'POST':
        body = request.body.decode('UTF-8').split('\n')
        print(body)
        params = []
        for i in range(5):
            try:
                if body[i] not in ['','\r']:
                    params.append(body[i])
                else:
                    params.append('Не указан') # на случай корявого ввода
            except Exception:
                params.append("Не указан")

        products_list.append(Product(
            name=params[0],
            category=params[1],
            price=params[2],
            animal=params[3],
            weight=params[4]
        ))

        return HttpResponse(str(products_list[-1]), status=200)

def product(request: HttpResponse, id:int):
    if request.method == 'GET':
        try:
            answer = products_list[id]
        except Exception:
            return Http404()
        
        if answer != None: return HttpResponse(str(answer), status=200)
        return HttpResponseRedirect(reverse('products'))

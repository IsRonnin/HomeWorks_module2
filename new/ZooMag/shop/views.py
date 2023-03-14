from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect, StreamingHttpResponse, FileResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from .models import Product, Category
import os

import random


APP_DIR = Path(__file__).resolve().parent
our_static = os.path.join(APP_DIR, 'static')


category_img = {"сухой_корм": os.path.join(our_static, 'images', 'dry_food.jpg'),
                    "корм":os.path.join(our_static, 'images', 'food.jpg'),
                    "паучи": os.path.join(our_static, 'images', 'pauchi.jpeg')}


# ITS TERRIBLE!
# print(products_dict)
# Костыль мля!
# print(category_dict) # а это вам для проверки

def get_product(id: int):
    try:
        obj = Product.objects.get(pk = id)
    except Product.DoesNotExist:
        obj = Http404()
    return obj
def get_category(name: str):
    try:
        return Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise Http404()
    


def start_page(request: HttpRequest):
    return HttpResponse('<a href="hello/">Дз_1</a><br><a href="products/">Список товаров</a> <br>' + 
                        '<br>'.join(f'<a href="products/product/{indx}">Продукт: {indx}</a><br>'.format(products_list[indx]) if products_list[indx] != None 
                                    else f'<a href="products/product/{indx}">Продукт: None</a><br>'.format(products_list[indx]) 
                                    for indx in range(len(products_list))).join(["<a href=categories/>Картиночки!</a><br><br>",
                                                                                "<br>Не стукайте ;3"]), status=200)


@csrf_exempt
def products(request:HttpRequest):
    if request.method == 'GET':
        #print('<br>'.join(str(product) for product in products_list))
        return StreamingHttpResponse('<br>'.join(str(product) for product in products_list), status=200)
    
    if request.method == 'POST':
        body = request.body.decode('UTF-8').split('\n')
        #print(body)
        params = []
        for i in range(5):
            try:
                if body[i] not in ['','\r']:
                    params.append(body[i])
                else:
                    params.append('Не указан') # на случай корявого ввода
            except Exception:
                params.append("Не указан")

        #products_list.append(Product(
        #    name=params[0],
        #    category=params[1],
        #    price=params[2],
        #    animal=params[3],
        #    weight=params[4]
        #))

        return HttpResponse(str(products_list[-1]), status=200)

def product(request: HttpResponse, id:int):
    if request.method == 'GET':
        try:
            answer = products_list[id]
        except Exception:
            return HttpResponse("<h1>Опачки... 404 вам!</h1>", status = 404)
        
        if answer != None: return HttpResponse(str(answer), status=200)
        return HttpResponseRedirect(reverse('products'))


from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect, StreamingHttpResponse, FileResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .myClass import *
import random

category_img = {"сухой_корм": 'C:/Users/artem/Desktop/Home_worksM2/2/again/web_work/ZooMag/shop/static/images/dry_food.jpg',
                    "корм":'C:/Users/artem/Desktop/Home_worksM2/2/again/web_work/ZooMag/shop/static/images/food.jpg',
                    "паучи": 'C:/Users/artem/Desktop/Home_worksM2/2/again/web_work/ZooMag/shop/static/images/pauchi.jpeg'}

products_list = filled()
products_list.append(None)

# ITS TERRIBLE!

products_dict = Product.big_dict()
category_dict = Product.category() # Формат - Категория: [id] Мы же вроде по id получаем?
# print(products_dict)
# Костыль мля!
# print(category_dict) # а это вам для проверки

def get_product(id: int):
    try:
        obj = [i for i in products_list if i != None and i.id == id][0]
    except:
        obj = None
    return obj
    
def hello(request: HttpRequest):
    obj = Product("Royal Canin", "Сухой корм", "600 ₽", "Коты", '1000 г') # Условный обьект.
    my_info = f'Я {"Артём Ващенко"} мне {"15"} и я люблю кодить! Вот вам случайное число! <{random.randint(-1000, 1000)}> <br>' + str(obj)
    return HttpResponse(my_info, status=200)

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
            return HttpResponse("<h1>Опачки... 404 вам!</h1>", status = 404)
        
        if answer != None: return HttpResponse(str(answer), status=200)
        return HttpResponseRedirect(reverse('products'))

def image_view(request: HttpRequest):
    respounse = FileResponse(open('C:/Users/artem/Desktop/Home_worksM2/2/again/web_work/ZooMag/shop/static/images/1.png', 'rb'))
    return respounse

def get_img_category(request: HttpRequest, category: str):
    if  category.lower() in category_img:   
        respounse = FileResponse(open(category_img[category.lower()], 'rb'))
    else:
        respounse = HttpResponse("<h1>Опачки... 404 вам!</h1>", status = 404)
    return respounse

def get_all_categories(request: HttpRequest):
    answer = ''.join([f"<a href={i}>{i}</a><br>" for i in category_img])
    return HttpResponse(answer, status = 200)


def json_view(request: HttpRequest, id: int):
    if request.method == 'GET':
        product = get_product(id)
        if product == None:
            respounse = HttpResponse("<h1>Опачки... 404 вам!</h1>", status = 404)
        product.to_json()
        return FileResponse(open(f'shop/dumps/{id}.json', 'rb'),as_attachment=True)

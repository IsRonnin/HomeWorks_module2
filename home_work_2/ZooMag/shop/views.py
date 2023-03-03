from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
# Create your views here.
class Product:
    __MAX_ID = 0 # Приватная (Инкапсулированная) переменная-атрибут класса для счёта id
    def __init__(self, name, category, price, animal, weight) -> None: 
        self.name = name                
        self.category: str = category   
        self.id: int = Product.__MAX_ID 
        self.price = price
        self.animal = animal
        self.weight = weight

        Product.__MAX_ID += 1 
    def __str__(self):
        return f'''<br> Наименование - {self.name}<br> Категория - {self.category} <br> Цена - {self.price} <br> для кого? - {self.animal}<br>
        Вес - {self.weight}'''
    
def hello(request: HttpRequest):
    obj = Product("Royal Canin", "Сухой корм", "600 ₽", "Коты", '1000 г') # Условный обьект.
    my_info = f'Я {"Артём Ващенко"} мне {"15"} и я люблю кодить! Вот вам случайное число! <{random.randint(-1000, 1000)}> <br>' + str(obj)
    return HttpResponse(my_info)

def start_page(request: HttpRequest):
    return HttpResponse('<a href="hello/">Клик меня!</a>')
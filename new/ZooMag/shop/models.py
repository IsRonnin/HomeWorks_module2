from django.db import models


import json, os

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="название", unique=True, blank=True)
    author = models.CharField(max_length=200, verbose_name="производитель", blank=True)
    category = models.ForeignKey(
        "Category",
        verbose_name="категория",
        null=True,
        on_delete=models.SET_NULL
    )
    release_dat = models.DateField(verbose_name="дата производства")
    
    def __str__(self):
        return f'''<br> Наименование - {self.name}<br> 
        Категория - {self.category} <br> Цена - {self.price} 
        <br> для кого? - {self.animal}<br>
        Вес - {self.weight}'''
    
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="название", unique=True, blank=True)
    image = models.ImageField(verbose_name="изображение", upload_to='categories')


my_dict = {"Royal Canin": {"category": "Сухой корм", "price": "600 ₽", "animal": "Коты", "weight": '1000 г'}, 
           "SAVITA консервы консервы": {"category": "Корм", "price": "152 ₽", "animal": "Коты", "weight": '100 г'}, 
           "Organix мясное суфле с ягнёнком": {"category": "Корм", "price": "61 ₽", "animal": "Котята ", "weight": '125 г'},
           "Royal Canin паучи кусочки в соусе": {"category": "Паучи", "price": "1680 ₽", "animal": "Коты ", "weight": '85 г'}}


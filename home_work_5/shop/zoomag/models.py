from django.db import models
import json

class Product(models.Model):

    name = models.CharField(max_length=50, blank=False, unique=True, verbose_name="имя")       
    category = models.ForeignKey(
        'Category',
        null=True,
        verbose_name="категория",
        on_delete = models.SET_NULL
    )
    price = models.CharField(max_length=100, blank=False, verbose_name="цена")
    animal = models.CharField(max_length=100, blank=False, verbose_name="животное")
    weight = models.CharField(max_length=100, blank=False, verbose_name="вес")
    release_date = models.DateField(auto_now_add = True, verbose_name="дата производства")

    def __str__(self):
        return f''',,имя - {self.name},Категория {self.category},Цена {self.price},Животное{self.animal}<br>вес {self.weight},время выхода {self.release_date},путь к картинке {self.category.image}'''.replace(',', '<br>')
    def to_dic(self):
        return {
            "id": self.pk,
            "name": self.name,
            "category": self.category.name,
            "price": self.price,
            "animal": self.animal,
            "weight": self.weight,
            "release_date": str(self.release_date)
        }

    def to_json(self):
        with open(f'zoomag/dumps/{self.pk}.json', 'w+') as file:
            json.dump(self.to_dic(), file)

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='имя', unique=True)
    image = models.ImageField(upload_to="categories", verbose_name="изображение")
    def __str__(self):
        return f"{self.name}"



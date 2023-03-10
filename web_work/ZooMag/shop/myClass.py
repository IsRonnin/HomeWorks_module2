import json, os

class Product:
    __MAX_ID = 0 # Приватная (Инкапсулированная) переменная-атрибут класса для счёта id
    __private_class_dict  = {}
    def __init__(self, name='None', category='None', price='None', animal='None', weight='None') -> None: 
        self.name = name                
        self.category: str = category   
        self.id: int = Product.__MAX_ID 
        self.price = price
        self.animal = animal
        self.weight = weight
        Product.__private_class_dict.update(self.to_dict())
        
        Product.__MAX_ID += 1 
    def __str__(self):
        return f'''<br> Наименование - {self.name}<br> Категория - {self.category} <br> Цена - {self.price} <br> для кого? - {self.animal}<br>
        Вес - {self.weight}'''
    
    def to_dict(self) -> dict:
        return{self.id :{"Наименование": self.name, "Категория": self.category,
                                          "Цена": self.price, "Животное": self.animal,
                                          "Вес": self.weight}}
    
    def to_json(self):
        data = self.to_dict()
        print(data)
        with open(f'shop/dumps/{self.id}.json', 'w') as f:
            json.dump(data, f)

    @classmethod
    def big_dict(self) -> dict:
        return Product.__private_class_dict
    @classmethod
    def category(self) -> dict:
        products_dict = Product.__private_class_dict
        category = {products_dict[i]["Категория"]: [ki for ki in products_dict.keys() 
                                            if products_dict[ki]["Категория"] == products_dict[i]["Категория"]] for i in products_dict.keys()}
        return category

my_dict = {"Royal Canin": {"category": "Сухой корм", "price": "600 ₽", "animal": "Коты", "weight": '1000 г'}, 
           "SAVITA консервы консервы": {"category": "Корм", "price": "152 ₽", "animal": "Коты", "weight": '100 г'}, 
           "Organix мясное суфле с ягнёнком": {"category": "Корм", "price": "61 ₽", "animal": "Котята ", "weight": '125 г'},
           "Royal Canin паучи кусочки в соусе": {"category": "Паучи", "price": "1680 ₽", "animal": "Коты ", "weight": '85 г'}}


def filled() -> list:
    products = []
    for product in my_dict.keys():
        #print(product, my_dict[product])
        products.append(Product(product, my_dict[product]["category"], my_dict[product]["price"],
                                my_dict[product]["animal"], my_dict[product]["weight"]))
    return products

from pynput import keyboard

# Зоомагазин поле 1 - цена товара 2 - для какого животного 3 - вес
class Product:
    __MAX_ID = 0 # Приватная (Инкапсулированная) переменная-атрибут класса для счёта id
    def __init__(self, name, category, price, animal, weight) -> None: # Господа! те кто берут код с моего гитхаба! обратите внимание что 
                                                                       # у вас тема может отличатся от моей и код нужно чутка переделать! 
                                                                       # что нужно изменить думаю знаете (по таблице из доков с дз прикреплена
                                                                       # к гиту)
        self.name = name # обьявляем атрибут класса self.name присваивая ему значение переданного аргумента name
        self.category: str = category # аналогично тому что выше 
        self.id: int = Product.__MAX_ID # Присваиваем аттрибуту self.id значение класса product.__MAX_ID (Описанно выше)
        # новые аттрибуты
        self.price = price
        self.animal = animal
        self.weight = weight

        Product.__MAX_ID += 1 # увеличиваем глобальный классовы атрибут на 1 (что бы следующий id был больше на 1 и не повторялся)

my_dict = {"Royal Canin": {"category": "Сухой корм", "price": "600 ₽", "animal": "Коты", "weight": '1000 г'}, 
           "SAVITA консервы консервы": {"category": "Консервы", "price": "152 ₽", "animal": "Коты", "weight": '100 г'}, 
           "Organix мясное суфле с ягнёнком": {"category": "Ламистер", "price": "61 ₽", "animal": "Котята ", "weight": '125 г'},
           "Royal Canin паучи кусочки в соусе": {"category": "Паучи", "price": "1680 ₽", "animal": "Коты ", "weight": '85 г'}}

products = [] # создаём обьекты класса
print(my_dict.keys())
for product in my_dict.keys():
    print(f"product : {product}")
    #print(product, my_dict[product])
    products.append(Product(product, my_dict[product]["category"], my_dict[product]["price"],
                            my_dict[product]["animal"], my_dict[product]["weight"]))


print(*[                        # их вывод через краткий for (о нём подробнее можно узанать у меня или в закреалённой статье)
    (product.id, product.name, product.category, product.price, product.animal, product.weight) # обращение к полю name 
    for product in products     # обьявляем product вытягивая его из списка products
    if len(product.name) > 2    # проверяем если количество буков в product.name > 2 если да выполняем строку которая выше.
], sep='\n')                    # делим вывод на разные строки в консоли

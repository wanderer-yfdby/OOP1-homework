# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.

#Шаги:
#1. Создай класс `Store`:

#-Атрибуты класса:
#- `name`: название магазина.
#- `address`: адрес магазина.
#- `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.

#- Методы класса:
#- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
#-  метод для добавления товара в ассортимент.
#- метод для удаления товара из ассортимента.
#- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
#- метод для обновления цены товара.

#2. Создай несколько объектов класса `Store`:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item = {}
    def add_item(self, item_name, price):
        self.item[item_name] = price
        print(f"товар {item_name} был добавлен в магазине {self.name}")
    def remove_item(self, item_name):
        if item_name in self.item:
            del self.item[item_name]
            print(f"товар {item_name} удален из магазина {self.name}")
    def get_price(self, item_name):
        if self.item == None:
            print(f"товар {item_name} не найден")
        else:
            print(f"Цена на {item_name} в магазине {self.name} сегодня: {self.item.get(item_name)} ")
    def update_price(self, item_name, new_price):
        if item_name in self.item:
            self.item[item_name] = new_price
            print(f"цена на товар {item_name} обновлена в магазине {self.name}")
        else:
            print(f"товар {item_name} не найден")

store1 = Store("Чижик", "Волгоградская 47")
store2 = Store("Монетка", "Амундсена 66")
store3 = Store("Верный", "Бардина 38")


store3.add_item("кефир", 44)
store3.add_item("батон", 34)
store2.add_item("шоколад", 69)
store2.add_item("сыр", 79)
store1.add_item("творог", 64)
store1.add_item("кефир", 43)

store1.remove_item("кефир")
print(store1.get_price("кефир"))
print(store1.get_price("творог"))
store3.update_price("кефир", 46)
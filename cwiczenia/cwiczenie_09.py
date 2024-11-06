"""
Zaimplementuj klasę Product przechowującą informację o cenie,
nazwie oraz ID produktu.
Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
Przykład użycia:

>>> product = Product(1, 'Woda', 10.99)
>>> product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN

"""

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.id}, cena: {self.price} PLN')
"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w
określonej liczbie do koszyka. Zaimplementuj metodę obliczającą
całkowitą wartość koszyka oraz wypisującą informację o zawartości
koszyka. Dodanie dwa razy tego samego produktu do koszyka
powinno stworzyć tylko jedną pozycję.

Przykład użycia:
>>> basket = Basket()
>>> product = Product(1, 'Woda', 10.00)
>>> product2 = Product(2, 'Cola', 20.00)
>>> basket.add_product(product, 5)
>>> basket.add_product(product2, 10)
>>> basket.count_total_price()
250.0
>>> basket.generate_report()
Produkty w koszyku:
- Woda (1), cena: 10.00 x 5
- Cola (2), cena: 20.00 x 10
W sumie: 250.00
"""


class Basket:
    def __init__(self):
        self.basket_entries = []

    def list_products(self):
        for basket_entry in self.basket_entries:
            print(basket_entry)

    def add_product(self, product: "Product", count: int):
        for basket_entry in self.basket_entries:
            if basket_entry.product == product:
                basket_entry.count += count
                return
        self.basket_entries.append(BasketEntry(product, count))

    def count_total_price(self):
        total_price = 0
        for basket_entry in self.basket_entries:
            total_price += basket_entry.price()
        return total_price

    def generate_report(self):
        raport = "Produkty w koszyku:\n"

        for be in self.basket_entries:
            raport += be.raport()

        raport += f"W sumie: {self.count_total_price():.2f}"
        return raport



class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price


class BasketEntry:
    def __init__(self, product: Product, count: int):
        self.product = product
        self.count = count

    def price(self) -> float:
        return self.product.price * self.count

    def raport(self) -> str:
        return f"- {self.product.name} ({self.product.id}), cena: {self.product.price:.2f} x {self.count}\n"



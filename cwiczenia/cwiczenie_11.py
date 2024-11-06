"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w
określonej liczbie do koszyka. Zaimplementuj metodę obliczającą
całkowitą wartość koszyka oraz wypisującą informację o zawartości
koszyka. Dodanie dwa razy tego samego produktu do koszyka
powinno stworzyć tylko jedną pozycję.
Przykład użycia:
>>> basket = Basket()
>>> product = Product(1, 'Woda', 10.00)
>>> basket.add_product(product, 5)
>>> basket.count_total_price()
50.0
>>> basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00

"""
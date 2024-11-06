from cwiczenie_11 import Basket, Product


def test_basket():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    product2 = Product(2, 'Cola', 20.00)
    basket.add_product(product, 5)
    basket.add_product(product2, 10)
    assert basket.count_total_price() == 250
    expected = 'Produkty w koszyku:\n- Woda (1), cena: 10.00 x 5\n- Cola (2), cena: 20.00 x 10\nW sumie: 250.00'

    assert basket.generate_report() == expected


def test_basket_add_the_same_product_many_times():
    basket = Basket()
    product = Product(1, 'Woda', 10.00)
    basket.add_product(product, 5)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 100
    expected = 'Produkty w koszyku:\n- Woda (1), cena: 10.00 x 10\nW sumie: 100.00'
    assert basket.generate_report() == expected



def test_basket_add_the_same_product_many_times_product_defined_twice():
    basket = Basket()
    product1 = Product(1, 'Woda', 10.00)
    product2 = Product(1, 'Woda', 10.00)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert basket.count_total_price() == 100
    expected = 'Produkty w koszyku:\n- Woda (1), cena: 10.00 x 10\nW sumie: 100.00'
    assert basket.generate_report() == expected
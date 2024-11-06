"""

Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinnymieć możliwość dodawania, odejmowania, mnożenia (przez inny
wektor i przez liczbę), porównywania (po długości) oraz powinny
posiadać czytelną reprezentację napisową.
Przykład użycia:


vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
vector_4 = vector_1 - vector_2
vector_1 * vector_2 => Vector(1, 4)
vector_1 * 5 => Vector(5, 10)

isinstance

__add__ => +

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"<Vector x={self.x} y={self.y}>"
print(Vector(1, 2))
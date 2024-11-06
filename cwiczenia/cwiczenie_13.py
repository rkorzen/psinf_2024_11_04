"""

Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinnymieć możliwość dodawania, odejmowania, mnożenia (przez inny
wektor i przez liczbę), porównywania (po długości) oraz powinny
posiadać czytelną reprezentację napisową.
Przykład użycia:


vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2  __add__
vector_4 = vector_1 - vector_2  __sub__
vector_1 * vector_2 => Vector(1, 4) __mul__
vector_1 * 5 => Vector(5, 10)  __mul__

vector_1 == vector_2   __eq__
vector_1 > vevtor_2    __gt__
vector_1 >= vevtor_2   __ge__


isinstance

__add__ => +

"""

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return ((self.x**2) + (self.y**2))**0.5

    def __repr__(self):
        return f"<Vector x={self.x} y={self.y}>"

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__class__(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.__class__(self.x * other.x, self.y * other.y)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.length() == other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

if __name__ == "__main__":
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = Vector(x=1, y=3)
    assert vector_1 + vector_2 == Vector(2, 4)
    assert vector_1 - vector_2 == Vector(0, 0)
    assert vector_1 * vector_2 == Vector(1, 4)
    assert vector_1 * 5 == Vector(5, 10)
    assert 5 * vector_1 == Vector(5, 10)

    assert vector_1 == vector_2
    assert vector_1 < vector_3
    assert vector_3 >= vector_1
    assert vector_3 >= vector_3

    print(vector_1)
    print([vector_1, vector_2])

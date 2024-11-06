""""

class <NazwaKlasy>:
    atrybut_klasy = 1

    # metoda instancji
    def foo(self):
      pass

"""

class Kwadrat:
    # metoda
    def __init__(self, bok):
        self.bok = bok
        self.color = "red"

    def policz_obowod(self):
        return self.bok * 4

    def __eq__(self, other):
        return self.bok == other.bok and self.color == other.color


kwadrat1 = Kwadrat(2)
kwadrat2 = Kwadrat(2)
kwadrat3 = Kwadrat(300)

print(kwadrat1.bok)
print(kwadrat2.bok)
print(kwadrat3.bok)

print(kwadrat1.policz_obowod())
print(Kwadrat.policz_obowod(kwadrat3))

print(kwadrat1 == kwadrat2)
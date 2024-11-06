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

    @property
    def bok(self):
        return self._bok

    @bok.setter
    def bok(self, value):
        if value < 0:
            raise ValueError("Bok nie moze byc mniejszy niz 0")
        self._bok = value

    @property
    def obwod(self):
        return self.bok * 4

    @obwod.setter
    def obwod(self, value):
        if value < 0:
            raise ValueError("Obwod nie moze byc mniejszy niz 0")
        self.bok = value / 4

    def __eq__(self, other):
        return self.bok == other.bok and self.color == other.color


kwadrat1 = Kwadrat(2)
kwadrat2 = Kwadrat(2)
kwadrat3 = Kwadrat(300)
print(kwadrat1.bok)
print(kwadrat1.bok)
print(kwadrat2.bok)
print(kwadrat3.bok)

print(kwadrat1.obwod)
kwadrat1.bok = -50
print(kwadrat1.obwod)

kwadrat1.obwod = 400
print(kwadrat1.bok)
print(kwadrat1 == kwadrat2)

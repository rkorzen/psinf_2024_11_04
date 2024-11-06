class Foo:

    def __init__(self):
        self.x = 1
        self._x = 2
        self.__x = 3

    def _zrob_cos(self):
        print("Metoda prywatna")

    def wywolaj_zrob_cos(self):
        return self._zrob_cos()

    def get_x(self):
        return self.__x

f = Foo()

print(f.x)
print(f._x)
print(dir(f))
print(f._Foo__x)
# print(f.__x)

f.x = 10
f._x = 100
f.__x = 1000

print(f.__x)
print(f._Foo__x)
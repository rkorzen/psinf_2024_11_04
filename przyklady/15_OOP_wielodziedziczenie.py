

class Hero:

    def __init__(self, name):
        self.name = name


class FlyableMixin:

    def fly(self):
        print("czy to ptak? czy to samolot? NIe to lata super hero")


class StrenghtMixin:
    def super_strength(self):
        print("jest super silny")


class FastMixin:
    def super_fast(self):
        print("jest super szybki")


class PsychokineticMixin:

    def psychokinetic(self):
        print("jest psychokinetic")


class Superman(Hero, FlyableMixin, StrenghtMixin, FastMixin):
    pass


class Marsian(Hero, FlyableMixin, PsychokineticMixin):
    pass


class A:

    def foo(self):
        print("foo z A")

class B:

    def foo(self):
        print("foo z B")

class C(A, B):
    pass


c = C()
c.foo()

print(C.mro())
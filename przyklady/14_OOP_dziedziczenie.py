
class Animal:

    def __init__(self, name):
        self.name = name
        self.energy = 100

    def sleep(self):
        self.energy += 10

    def eat(self):
        self.energy += 20

    def run(self):
        self.energy -= 20

    def make_sound(self):
        print(f"I am {self.name} and my sound is ...")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Hau Hau")


class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Miau Miau")

a = Animal("Diplodok")
d = Dog("Reksio")
c = Cat("Mruczek")


a.sleep()
d.run()
c.eat()


a.make_sound()
d.make_sound()
c.make_sound()
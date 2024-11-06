"""
Zaimplementuj klasę PremiumEmployee, która będzie klasą
pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
przyznawanie bonusów pracownikowi.
>>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
>>> employee.register_time(5)
>>> bonus = AmountBonus(1000.0)
>>> employee.give_bonus(bonus)
>>> employee.give_bonus(PercentBonus(10))
>>> employee.pay_salary()
1650.0

"""

from cwiczenie_10 import Employee


class Bonus:

    def __init__(self, value):
        self.value = value


class PercentBonus(Bonus):
    def apply(self, to_pay):
        to_pay += to_pay * self.value / 100
        return to_pay


class AmountBonus(Bonus):
    def apply(self, to_pay):
        return to_pay + self.value


class PremiumEmployee(Employee):

    def __init__(self, first_name, last_name, rate_per_hour, bonus=None):
        super().__init__(first_name, last_name, rate_per_hour)

        self.bonuses = []
        if bonus:
            self.bonuses.append(bonus)

    def give_bonus(self, amount: int):
        self.bonuses.append(amount)

    def pay_salary(self):
        to_pay = super().pay_salary()

        for bonus in self.bonuses:
            to_pay = bonus.apply(to_pay)

        self.bonuses = []
        return to_pay

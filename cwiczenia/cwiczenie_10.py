"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej.

Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójną stawką godzinową).

Przykład użycia:

>>> employee = Employee('Jan', 'Nowak', 100.0)
>>> employee.pay_salary()
0.0
>>> employee.register_time(5)
>>> employee.pay_salary()
500.0
>>> employee.pay_salary()
0.0
>>> employee.register_time(10)
>>> employee.pay_salary()
1200.0

"""

class Employee:

    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0
        self.overhours = 0

    def register_time(self, hours):
        if hours > 8:
            self.worked_hours = 8
            self.overhours = hours - 8
        else:
            self.worked_hours = hours

    def pay_salary(self):
        salary = self.worked_hours * self.rate_per_hour + self.overhours * self.rate_per_hour * 2
        self.worked_hours = 0
        self.overhours = 0
        return salary

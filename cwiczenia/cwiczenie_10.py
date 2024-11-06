"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej.

Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójną stawką godzinową).

Przykład użycia:

>>> employee = Employee('Jan', 'Nowak', 100.0)
>>> employee.register_time(5)
>>> employee.pay_salary()
500.0
>>> employee.pay_salary()
0.0
>>> employee.register_time(10)
>>> employee.pay_salary()
1200.0

"""
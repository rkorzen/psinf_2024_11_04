"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i
wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu
przetrzymywany był w zmiennych prywatnych.
Przykład użycia:

> cash_machine = CashMachine()
> cash_machine.is_available
False
> cash_machine.put_money([200, 100, 100, 50])
> cash_machine.is_available
True
> cash_machine.withdraw_money(150)
[100, 50]
---
lista.append(1)
lista.extend([1, 2, 3])
lista.sort(reverse=True)

lista.remove(<value>)

"""

class CashMachine:


    def __init__(self):
        self._container = []

    def put_money(self, money: list[int]):
        self._container.extend(money)

    @property
    def is_available(self) -> bool:
        return bool(self._container)

    def withdraw_money(self, amount: int) -> list[int]:
        return self._container
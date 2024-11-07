"""

Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
* brak miejsca na banknoty (ustal limit banknotów w bankomacie)
* zła wartość wypłacanej sumy (musi być podzielna przez 10)
* brak odpowiednich banknotów w bankomacie

Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki.
Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.

Przykład użycia:

Podaj typ operacji: WYPŁATA
Podaj kwotę do wypłacenia: 150
BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!

"""


class CashMachineError(Exception):
    pass

class CashMachineFullError(CashMachineError):
    def __init__(self, limit):
        super().__init__(f"Brak miejsca na banknoty! Maksymalna liczba banknotów: {limit}")

class InvalidAmountError(CashMachineError):
    def __init__(self, amount):
        super().__init__(f"Kwota {amount} nie jest podzielna przez 10!")

class InsufficientFundsError(CashMachineError):
    def __init__(self, amount):
        super().__init__(f"Brak wystarczającej liczby banknotów dla kwoty {amount}!")

class CashMachine:
    MAX_BILLS = 100  # Ustalony limit liczby banknotów w bankomacie
    TYPE_OF_BILLS = [10, 20, 50, 100, 200, 500]

    def __init__(self):
        self._container = []

    def put_money(self, money: list[int]):
        if len(self._container) + len(money) > self.MAX_BILLS:
            raise CashMachineFullError(self.MAX_BILLS)

        for bill in money:
            if bill not in self.TYPE_OF_BILLS:
                raise InvalidAmountError(bill)

        self._container.extend(money)

    @property
    def is_available(self) -> bool:
        return bool(self._container)

    def withdraw_money(self, amount: int) -> list[int]:
        if amount % 10 != 0:
            raise InvalidAmountError(amount)

        bills_to_withdraw = []
        for bill in sorted(self._container, reverse=True):
            if sum(bills_to_withdraw) + bill <= amount:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) != amount:
            raise InsufficientFundsError(amount)

        for bill in bills_to_withdraw:
            self._container.remove(bill)
        return bills_to_withdraw

# Interfejs tekstowy
def main():
    atm = CashMachine()
    while True:
        try:
            operation = input("Podaj typ operacji (WPLATA lub WYPLATA): ").strip().upper()
            if operation == "WPLATA":
                money = input("Podaj nominały do wpłaty (oddzielone przecinkami): ")
                money_list = [int(bill.strip()) for bill in money.split(",")]
                atm.put_money(money_list)
                print("Pieniądze zostały wpłacone.")
            elif operation == "WYPLATA":
                amount = int(input("Podaj kwotę do wypłacenia: "))
                bills = atm.withdraw_money(amount)
                print(f"Wypłacone banknoty: {bills}")
            else:
                print("BŁĄD: Nieznana operacja. Spróbuj ponownie.")

        except ValueError:
            print("BŁĄD: Niepoprawna wartość. Spróbuj ponownie.")
        except CashMachineFullError as e:
            print(f"BŁĄD: {e}")
        except InvalidAmountError as e:
            print(f"BŁĄD: {e}")
        except InsufficientFundsError as e:
            print(f"BŁĄD: {e}")

if __name__ == "__main__":
    main()

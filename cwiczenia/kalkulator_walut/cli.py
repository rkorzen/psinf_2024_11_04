from kalkulator import get_codes, exchange

print("Witaj w kantorze")
print(f"Oferujemy waluty: {get_codes()}")

code = input("Podaj kod waluty, którą chcesz kupić: ")
ile = float(input("Ile tej waluty chcesz kupic: "))

print(f"Za zakup {ile} {code} zapłacisz {exchange(code, ile)}")




"""
Napisz program obsługujący bazę danych pracowników. W bazie
danych przechowuj imię, nazwisko, email, rok urodzenia, pensję.
Skorzystaj z modułu json.

Przykład użycia:


$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w
Pracownicy:

$ python cwiczenie_18.py
Co chcesz zrobić? [d - dodaj, w - wypisz] d
Imie: Jan
Nazwisko: Nowak
Rok urodzenia: 1980
Pensja: 5000.0

$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w
Pracownicy:
- [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN

"""
import json

try:
    with open('employees.json') as f:
        dane = json.load(f)
except FileNotFoundError:
    dane = []


action = input("Co chcesz zrobić? [d - dodaj, w - wypisz]: ")

if action == "d":

    first_name = input("Imie: ")
    last_name = input("Nazwisko: ")
    b_year = int(input("Rok urodzenia: "))
    salary = float(input("Pensja: "))

    employee = {
        "first_name": first_name,
        "last_name": last_name,
        "b_year": b_year,
        "salary": salary
    }

    dane.append(employee)
    with open("employees.json", "w") as file:
        json.dump(dane, file)

elif action == "w":
    print("Pracownicy: ")
    for i, employee in enumerate(dane, start=1):
        print(f"- [{i}] {employee['first_name']} {employee['last_name']} - rok: {employee['b_year']}, pensja: {employee['salary']:.2f} PLN")

"""
Utwórz 3 zestawy zmiennych opisujacych produkty
nazwa, cena, waga

nazwa_1 = "Chleb
cena_1 = 5.67
waga_1 = 1


stworz zmienna raport, która bedzie miala złaczone te informacje i ladne sformatowane

raport_1 = ""
raport_2 = ""
raport_3 = ""

raport = f'''
{raport_1}
{raport_2}
{raport_3}
'''

print(raport)

Chleb      1.00 kg   5.67 PLN
Pomarancza 2.20 kg  14.56 PLN
Jaja       3.20 kg 123.44 PLN


"""

nazwa_1 = "Chle23423423423rfgefg45rg454tgrgh45yb"
waga_1 = 1
cena_1 = 5.67

nazwa_2 = "Pomaranczafbe4rgdfbv45gdfg"
waga_2 = 2.2
cena_2 = 14.56

nazwa_3 = "Jaja"
waga_3 = 3.2
cena_3 = 123.44

print(len(nazwa_2))


# raport_1 = f"{nazwa_1:15} {waga_1:6.2f} kg {cena_1:6.2f} PLN"
# raport_2 = f"{nazwa_2:15} {waga_2:6.2f} kg {cena_2:6.2f} PLN"
# raport_3 = f"{nazwa_3:15} {waga_3:6.2f} kg {cena_3:6.2f} PLN"

# na wyrost:
dlugosc = max([len(nazwa_1), len(nazwa_2), len(nazwa_3)])

raport_1 = f"{nazwa_1:{dlugosc}} {waga_1:6.2f} kg {cena_1:6.2f} PLN"
raport_2 = f"{nazwa_2:{dlugosc}} {waga_2:6.2f} kg {cena_2:6.2f} PLN"
raport_3 = f"{nazwa_3:{dlugosc}} {waga_3:6.2f} kg {cena_3:6.2f} PLN"



raport = f"""
{raport_1}
{raport_2}
{raport_3}
"""

print(raport)
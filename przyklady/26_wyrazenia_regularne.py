import re

tekst = "1234abc"
wzorzec = r"\d+"

wynik = re.match(wzorzec, tekst)

print(wynik)
print(wynik.group())


text = "moj numer to 123-456-7890 xxx"
wzorzec = r"\d{3}-\d{3}-\d{4}"
wz2 = r"\d{3}"
wynik = re.search(wzorzec, text)
wynik2 = re.findall(wz2, text)
print(wynik.group())

print(wynik2)
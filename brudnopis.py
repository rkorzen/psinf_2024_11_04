
lista = [1, 2, 3]

print("-".join(map(str, lista)))

print("ala ma kota".encode())

print("zażółć gęśla jaźń".encode())

print("zażółć gęśla jaźń".encode("CP1250"))

moje_bytes = b'za\xbf\xf3\xb3\xe6 g\xea\x9cla ja\x9f\xf1'

print(moje_bytes)
print(moje_bytes.decode("CP1250"))


with open("dane_w_cp1250.txt", "w", encoding="cp1250") as f:
    f.write("""
A
B
C
Ą
ę
""")

from pprint import pprint
pprint(dir(str))
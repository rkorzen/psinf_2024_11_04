"""
while <warunek>:
   <blok instrukcji>

while True:
    <blok instrukcji>




"""

i = 0

while i < 10:
    print(i)
    i += 1



i = 0

while True:
    print(i)
    i += 1
    if i >= 10:
        break


i = 0

while i < 10:
    if i % 2 == 0:
        print(i)
        i+=1
        continue
    print(f"cos tam robie z liczba: {i}")
    i += 1

lista = [1, 2, 3, 4, 5]

i = 0
while i < len(lista):
    print(lista[i])
    i += 1


for el in lista:
    print(el)
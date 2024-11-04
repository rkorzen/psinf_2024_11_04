## Organizacja szkolenia

### Harmonogram przerw:

- **Przerwa poranna**: 10:30 - 10:45  
- **Przerwa obiadowa**: 12:15 - 12:45  
- **Przerwa popołudniowa**: 14:15 - 14:30  

---

## Narzędzia programistyczne

Podczas szkolenia będziemy korzystać z dwóch popularnych edytorów:

- **PyCharm** (wersja Community) – profesjonalne środowisko do programowania w Pythonie, oferujące wsparcie dla zaawansowanych funkcji debugowania i integracji z systemami kontroli wersji.
- **Visual Studio Code** – lekkie, elastyczne IDE, które można dostosować do własnych potrzeb dzięki szerokiemu zbiorowi rozszerzeń.

---

## REPL (Read-Eval-Print Loop)

REPL to interaktywne środowisko uruchamiania kodu Python, które umożliwia szybkie testowanie fragmentów kodu. Proces działania:

1. **Read** – wprowadzenie wyrażenia przez użytkownika,
2. **Eval** – ocena wyrażenia przez interpreter,
3. **Print** – wyświetlenie wyników,
4. **Loop** – powtórzenie procesu.

Można korzystać z REPL w terminalu, wpisując `python` lub `python3`, co pozwala na natychmiastowe sprawdzenie działania kodu.

---

## Podstawy języka Python

Python to wszechstronny język programowania, który umożliwia używanie różnych paradygmatów, takich jak:

- **Proceduralne** – organizowanie kodu w funkcje.
- **Funkcyjne** – wykorzystanie funkcji jako pierwszorzędnych obiektów.
- **Obiektowe** – korzystanie z klas i obiektów.

**Cechy języka:**
- **Interpretowany** – kod jest uruchamiany bezpośrednio przez interpreter, bez potrzeby wcześniejszej kompilacji.
- **Silne typowanie** – typy zmiennych nie są automatycznie konwertowane, co zwiększa bezpieczeństwo kodu.
- **Dynamiczne typowanie** – typ zmiennej określany jest w czasie działania programu.

Python jest ceniony za **wszechstronność** i **bogaty zbiór bibliotek**, co pozwala na zastosowanie go w różnych dziedzinach, takich jak analiza danych, tworzenie stron internetowych, sztuczna inteligencja czy automatyzacja procesów.

---

## Środowisko pracy

1. **Edytor**: Visual Studio Code lub PyCharm Community.
2. **Tworzenie wirtualnego środowiska** – umożliwia oddzielenie zależności projektu:

   ```bash
   python -m venv .venv
   ```

   - **Linux**: aktywacja środowiska  
     ```bash
     source .venv/bin/activate
     ```
   - **Windows**: aktywacja środowiska  
     ```bash
     .venv\Scripts\activate
     ```

---

## Krótki wstęp do GIT

Podstawowe komendy w systemie kontroli wersji GIT:

```bash
git init                      # inicjalizacja repozytorium
git remote add origin <adres> # dodanie repozytorium zdalnego

git status                    # sprawdzenie stanu repozytorium
git add <plik>                # dodanie konkretnego pliku
git add .                     # dodanie wszystkich plików

git commit                    # wykonanie commita
git commit -m "<wiadomość>"   # commit z wiadomością
git commit -a --amend         # modyfikacja poprzedniego commita

git diff                      # pokazanie różnic
git log                       # historia commitów
git push <origin> <branch>    # wysłanie zmian na serwer

git pull                      # pobranie zmian z serwera
git pull <origin> <branch>    # pobranie zmian z wybranej gałęzi
```

---

## Podstawy Pythona

### Zmienne

Zmienne przechowują wartości i pozwalają na ich późniejsze użycie. Nazwa zmiennej może zawierać litery, cyfry oraz znak podkreślenia `_`, lecz nie może zaczynać się od cyfry.

**Przykłady:**

```python
osoba_1 = "Rafał"  # Poprawnie
1_osoba = "Rafał"  # Błędnie - zaczyna się od cyfry
```

### Typy wbudowane w Pythonie

Python oferuje różnorodne typy danych, które pozwalają na elastyczne przechowywanie i manipulowanie informacjami. Poniżej omówiono najważniejsze typy wraz z przykładami ich tworzenia oraz podstawowych operacji.

#### 01. **Napisy** (`str`)
- Używane do przechowywania tekstu. Napisy są sekwencjami znaków i mogą być tworzone za pomocą pojedynczych (`'`) lub podwójnych (`"`) cudzysłowów.

**Przykłady tworzenia i operacji:**
```python
napis = "Witaj, świecie!"
napis2 = 'Python jest świetny'
print(napis[0])       # Wypisze: 'W' (pierwszy znak)
print(len(napis))     # Długość napisu
print(napis.upper())  # Witaj, ŚWIECIE!
print(napis.replace("świat", "Python"))  # Witaj, Python!
```

#### 02. **Napisy jako kolekcje**
- Napisy traktowane są jako sekwencje znaków, co oznacza, że można odwoływać się do poszczególnych znaków za pomocą indeksu, a także iterować po nich.

**Przykłady operacji:**
```python
tekst = "Python"
print(tekst[1])       # Drugi znak: 'y'
for znak in tekst:
    print(znak)       # Wypisze każdy znak w osobnej linii
```

#### 03. **Napisy – inne tematy**
- Python oferuje różne metody umożliwiające manipulację napisami. Na przykład `.upper()`, `.lower()`, `.replace()`, `.split()`, czy `.strip()`.

**Przykłady operacji:**
```python
tekst = " Python jest świetny "
print(tekst.strip())       # Usuwa białe znaki na początku i końcu: "Python jest świetny"
print(tekst.split())       # ['Python', 'jest', 'świetny']
print(tekst.find("jest"))  # Znajduje indeks początku podciągu "jest": 7
```

#### 04. **Liczby całkowite** (`int`)
- Służą do przechowywania liczb całkowitych, zarówno dodatnich, jak i ujemnych.

**Przykłady operacji:**
```python
liczba = 42
liczba2 = -10
print(liczba + liczba2)  # Dodawanie: 32
print(liczba * 2)        # Mnożenie: 84
print(liczba // 5)       # Dzielenie całkowite: 8
```

#### 05. **Liczby zmiennoprzecinkowe** (`float`)
- Używane do przechowywania liczb z miejscami po przecinku, np. 3.14, -0.001.

**Przykłady operacji:**
```python
liczba = 3.14
liczba2 = -0.001
print(liczba + liczba2)  # Dodawanie: 3.139
print(liczba * 10)       # Mnożenie: 31.4
```

#### 06. **Liczby zespolone** (`complex`)
- Python pozwala również na operacje na liczbach zespolonych. Liczby zespolone zawierają część rzeczywistą i urojoną (np. `3 + 4j`).

**Przykłady operacji:**
```python
liczba_zespolona = 3 + 4j
print(liczba_zespolona.real)  # Część rzeczywista: 3.0
print(liczba_zespolona.imag)  # Część urojona: 4.0
print(liczba_zespolona.conjugate())  # Sprzężenie zespolone: (3-4j)
```

#### 07. **Kolekcje**

##### **Krotki** (`tuple`)
- Niezmienne sekwencje elementów. Raz utworzona krotka nie może być modyfikowana.

**Przykłady tworzenia i operacji:**
```python
krotka = (1, 2, 3)
print(krotka[0])      # Pierwszy element: 1
# krotka[0] = 5       # Błąd - krotki są niemodyfikowalne
print(len(krotka))    # Długość krotki: 3
```

##### **Listy** (`list`)
- Zmienne sekwencje, które mogą zawierać różne typy elementów. Listy można modyfikować.

**Przykłady tworzenia i operacji:**
```python
lista = [1, 2, 3]
lista.append(4)       # Dodanie elementu na końcu
lista[0] = 10         # Zmiana pierwszego elementu
print(lista)          # [10, 2, 3, 4]
print(lista.pop())    # Usuwa ostatni element i go zwraca: 4
```

##### **Zbiory** (`set`)
- Nieuporządkowane kolekcje unikalnych elementów, nie zawierają duplikatów.

**Przykłady tworzenia i operacji:**
```python
zbior = {1, 2, 3, 3}  # Duplikaty są automatycznie usuwane
zbior.add(4)          # Dodanie elementu do zbioru
zbior.remove(1)       # Usunięcie elementu
print(zbior)          # {2, 3, 4}
```

##### **Słowniki** (`dict`)
- Kolekcje par klucz-wartość, w których klucze muszą być unikalne.

**Przykłady tworzenia i operacji:**
```python
slownik = {'imie': 'Rafał', 'wiek': 30}
print(slownik['imie'])         # Wypisze wartość klucza 'imie': 'Rafał'
slownik['miasto'] = 'Warszawa' # Dodanie nowej pary klucz-wartość
print(slownik.keys())          # Wypisze klucze: dict_keys(['imie', 'wiek', 'miasto'])
print(slownik.values())        # Wypisze wartości: dict_values(['Rafał', 30, 'Warszawa'])
```



### Podobieństwa i różnice między kolekcjami

**Podobieństwa:**
- **Krotki** i **listy** są uporządkowane – zachowują kolejność elementów.
- **Listy**, **krotki**, **zbiory** i **słowniki** umożliwiają iterowanie po elementach.
  
**Różnice:**
- **Mutowalność**: Listy i słowniki są mutowalne (można je zmieniać po utworzeniu), natomiast krotki i zbiory są niemutowalne.
- **Uporządkowanie**: Listy i krotki zachowują kolejność elementów, natomiast zbiory i słowniki są nieuporządkowane.
- **Elementy unikalne**: Zbiory przechowują tylko unikalne elementy, natomiast listy, krotki i słowniki mogą zawierać duplikaty.
- **Dostęp do elementów**: Do elementów listy i krotki można odwoływać się za pomocą indeksów, do elementów słownika – za pomocą kluczy. Zbiory nie pozwalają na bezpośrednie indeksowanie.


### 08. **Wyrażenia warunkowe**

Wyrażenia warunkowe pozwalają na podejmowanie decyzji w kodzie – różne bloki kodu mogą być wykonane w zależności od spełnienia określonych warunków.

#### Składnia i użycie:
- **`if`** – wykonuje blok kodu, jeśli warunek jest prawdziwy.
- **`elif`** – używane po `if`, sprawdza kolejny warunek, jeśli poprzedni był fałszywy.
- **`else`** – wykonuje blok kodu, jeśli wszystkie poprzednie warunki były fałszywe.

#### Przykłady:

```python
x = 10
y = 5

# Prosty przykład z if i else
if x > y:
    print("x jest większe niż y")
else:
    print("x jest mniejsze lub równe y")
# Wyjście: x jest większe niż y

# Użycie if, elif i else
z = 0
if x > y:
    print("x jest większe niż y")
elif x == y:
    print("x jest równe y")
else:
    print("x jest mniejsze niż y")
# Wyjście: x jest większe niż y

# Przykład zagnieżdżonego if
a = 5
if a > 0:
    if a % 2 == 0:
        print("a jest dodatnie i parzyste")
    else:
        print("a jest dodatnie i nieparzyste")
else:
    print("a jest liczbą niedodatnią")
# Wyjście: a jest dodatnie i nieparzyste
```

#### Operatory porównania i logiczne:
Wyrażenia warunkowe często używają operatorów porównania i logicznych:
- **Operatory porównania**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Operatory logiczne**: `and`, `or`, `not`.

```python
a = 4
b = 8
c = 4

if a < b and a == c:
    print("a jest mniejsze niż b i równe c")
# Wyjście: a jest mniejsze niż b i równe c
```

### 09. **Pętle**

Python oferuje dwa główne typy pętli do iteracji i powtarzania operacji: `for` i `while`.

#### Pętla `for`
Pętla `for` służy do iterowania przez sekwencje, takie jak listy, krotki, napisy, czy zakresy (`range`). Pętla `for` przechodzi przez każdy element sekwencji, wykonując zdefiniowany blok kodu dla każdego z nich.

**Składnia i przykłady:**

```python
# Iteracja przez listę
lista = [1, 2, 3, 4, 5]
for element in lista:
    print(element)
# Wyjście: 1 2 3 4 5

# Iteracja przez zakres liczb
for i in range(5):
    print(i)
# Wyjście: 0 1 2 3 4

# Iteracja przez napis
napis = "Python"
for litera in napis:
    print(litera)
# Wyjście: P y t h o n
```

#### Funkcja `range()` w pętlach `for`:
Funkcja `range()` jest używana do generowania sekwencji liczb i często wykorzystywana w pętlach `for`.

```python
# Podstawowe użycie
for i in range(5):  # od 0 do 4
    print(i)

# Zakres z określonym początkiem i końcem
for i in range(2, 6):  # od 2 do 5
    print(i)

# Zakres z krokiem
for i in range(1, 10, 2):  # liczby nieparzyste od 1 do 9
    print(i)
```

#### Pętla `while`
Pętla `while` powtarza blok kodu, dopóki warunek jest prawdziwy. Używa się jej, gdy nie znamy z góry liczby iteracji i warunek zatrzymania zależy od działania programu.

**Składnia i przykłady:**

```python
# Przykład z warunkiem liczbowym
i = 0
while i < 5:
    print(i)
    i += 1
# Wyjście: 0 1 2 3 4

# Przykład nieskończonej pętli (należy unikać bez warunku zakończenia)
while True:
    print("Pętla trwa wiecznie")
    break  # Kończy pętlę
```

#### `break` i `continue` w pętlach
- **`break`** – przerywa działanie pętli, nawet jeśli warunek jest nadal spełniony.
- **`continue`** – przerywa bieżącą iterację i przechodzi do następnej.

**Przykłady:**

```python
# Przerwanie pętli za pomocą break
for i in range(10):
    if i == 5:
        break
    print(i)
# Wyjście: 0 1 2 3 4

# Przejście do kolejnej iteracji za pomocą continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# Wyjście: 0 1 3 4
```

#### Zagnieżdżone pętle
Pętle mogą być zagnieżdżone, czyli jedna pętla może znajdować się wewnątrz drugiej. Jest to przydatne do iteracji przez złożone struktury danych, np. listy list.

**Przykład zagnieżdżonej pętli:**

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Wyjście:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

### Podsumowanie różnic między pętlami `for` i `while`:

| Cecha               | `for`                          | `while`                         |
|---------------------|--------------------------------|---------------------------------|
| Zastosowanie        | Przechodzenie przez sekwencje  | Powtarzanie kodu dopóki warunek jest spełniony |
| Główne słowo kluczowe | `for`                         | `while`                         |
| Liczba iteracji     | Zwykle znana wcześniej         | Może być nieznana wcześniej     |
| Zakończenie pętli   | Po zakończeniu sekwencji       | Kiedy warunek staje się fałszywy |

Pętle i wyrażenia warunkowe są podstawowymi elementami języka Python, które umożliwiają kontrolę przepływu programu. Dzięki nim możliwe jest tworzenie złożonych i elastycznych aplikacji.
import pickle

class X:
    a = 1

dane = {"liczba": 2, "tekst": X()}

# serializacja
with open("xxx.pickle", "wb") as f:
    pickle.dump(dane, f)

# deserializacja
with open("xxx.pickle", "rb") as f:
    odzyskane_dane = pickle.load(f)

print(odzyskane_dane)

print(odzyskane_dane["tekst"].a)
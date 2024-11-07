from pathlib import Path


p = Path("")

p2 = p / "data" / "xxx"
p2.mkdir(parents=True, exist_ok=True)
print(p2.exists())

p3 = p2 / "data.csv"


with p3.open("w")  as f:
    f.write("data")

for plik in p2.glob("*.csv"):
    print(plik)
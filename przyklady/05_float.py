# float
print(int())
print(float())

print(1.23)

print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 == 0.3)
print(round(1/3, 2))

# typ decimal
# from decimal import Decimal
# print(Decimal("0.1") + Decimal("0.1")  + Decimal("0.1")  == Decimal("0.3"))


print(1.1e-10)

print(float("-inf"), float("inf"))

print(float("nan"))

x = float("nan")
print(x == x)

print(float("-inf") < 10 < float("inf"))
print(float("-inf") < x < float("inf"))

print(1.67e308)
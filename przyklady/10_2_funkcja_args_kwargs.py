
def moja_funkcja(a, b, c=1):
    ...


moja_funkcja(1, 2)
moja_funkcja(1, 2, 3)
moja_funkcja(a=1, b=2)
moja_funkcja(b=1, a=2, c=10)

# moja_funkcja(10, a=11)
# moja_funkcja(a=10, 11)


def add(a, b, *inne, x=1, y=2, **kwargs):
    print(inne)
    print(kwargs)
    pass
add(1, 2,)
add(1, 2, 1)
add(1, 2, 1, 2, 3, 1, 2, 3)
add(1, 2, 1, 2)


add(a=1, b=2, c=3, d=4)
add(a=1, b=2, x=3, y=4)



def add(a: int, b:int, *, to_str=False) -> int | str:
    r = a + b
    if to_str:
        return str(r)
    return r

r = add(1, 2, to_str=True)
print(r, type(r))


r = add(1, 2, 10)
print(r, type(r))


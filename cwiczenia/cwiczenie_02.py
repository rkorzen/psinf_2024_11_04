"""
Na podstawie wartosci x i y
określ przybliżoną pozycję na planszy (patrz rysunek)


"""

x = 95
y = 9

MIN_Y = 0
MAX_Y = 100

MIN_X = 0
MAX_X = 100

PROG_X1 = 10
PROG_X2 = 90
PROG_Y1 = 10
PROG_Y2 = 90


if x > MAX_X or x < MIN_X or y > MAX_Y or y < MIN_Y:
    print("Poza plansza")
elif x <= PROG_X1 and y >= PROG_Y2:
    print("GLR")
elif x >= PROG_X2 and y >= PROG_Y2:
    print("GPR")
elif x >= PROG_X2 and y <= PROG_Y1:
    print("DPR")
elif x <= PROG_X1 and y <= PROG_Y1:
    print("LDR")
elif x <= PROG_X1:
    print("LK")
elif y >= PROG_Y2:
    print("GK")
elif x >= PROG_X2:
    print("PK")
elif y <= PROG_Y1:
    print("DK")
else:
    print("C")

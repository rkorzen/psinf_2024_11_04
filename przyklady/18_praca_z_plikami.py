
try:
    f = open("17_comprehensions.py")
    # for line in f:
    #    print(line)
    print(f.closed)
finally:
    f.close()
    print(f.closed)


with open("17_comprehensions.py") as f:
    print(f.closed)

print(f.closed)


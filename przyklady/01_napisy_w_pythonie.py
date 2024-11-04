# tworzenie napisów
# to jest komentarz
"to jest napis"
'To jest napis'

'' # to jest pusty napis
#'"  # to da nam błąd

print("\nA\nB\nC\n")

print(("A"
 "B"
 "C"))

print("""
A
B
C
""")
''''''

print(str(1))

# operacje na napisach

print("Ala" + "Kot")
print("Ala","Kot")

print("x" * 40)
# print("x" * "40")

# formatowanie napisów


print("%d xxx %s" % (1, "a"))
print("{} xxx {}".format(1, "a"))
print(f"{1} xxx {'a'}")


a = 1
b = "a"
print("%d xxx %s" % (a, b))
a = 1234
print("{:<10.3f} xxx {:15}".format(a, b))
print(f"{a:<10.3f} xxx {b:15}")




# tworzenie napisów
# to jest komentarz
"to jest napis"
"To jest napis"

""  # to jest pusty napis
#'"  # to da nam błąd

print("\nA\nB\nC\n")

print(("A" "B" "C"))

print(
    """
A
B
C
"""
)
""""""

print(str(1))

# operacje na napisach

print("Ala" + "Kot")
print("Ala", "Kot")

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


# print(dir(b))

print("ala".center(10))
print("ala".upper())
metody = [
    "count",
    "index",

    "find",

    "capitalize",
    "casefold",
    "center",

    "encode",
    "endswith",
    "expandtabs",

    "format",
    "format_map",

    "isalnum",
    "isalpha",
    "isascii",
    "isdecimal",
    "isdigit",
    "isidentifier",
    "islower",
    "isnumeric",
    "isprintable",
    "isspace",
    "istitle",
    "isupper",
    "join",
    "ljust",
    "lower",
    "lstrip",
    "maketrans",
    "partition",
    "removeprefix",
    "removesuffix",
    "replace",
    "rfind",
    "rindex",
    "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    "startswith",
    "strip",
    "swapcase",
    "title",
    "translate",
    "upper",
    "zfill",
]



print("1a!".isalnum())


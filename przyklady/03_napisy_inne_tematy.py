
# a = "123"
# print(id(a))
# b = a
# print(id(b))
# a = "234"
# print(id(a))

a = "123"
b = "123"
print(id(a) == id(b))

a = "123 123 asasas"
b = "123 123 asasas"
print(id(a) == id(b))

a = "hello world"
b = "hello world"
print(id(a) == id(b))

a = 10000000
b = 10000000.0

print(a == b)

print(a is b)
print(id(a) == id(b))

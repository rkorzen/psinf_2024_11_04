import sys

print(sys.path)

# import modul_b
# print(modul_b.x)
# print(modul_b.y)
print(dir())
from modul_b import x
print(dir())
print(x)
# print(y)

#
# from modul_b import *
# print(x)
# print(y)
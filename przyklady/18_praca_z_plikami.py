
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

help(open)

with open("dane.txt", "w") as f:
    f.write("b")


import os
help(os.fstat)
def is_file_descriptor(f):
    try:
        os.fstat(f)
        return True
    except (TypeError, ValueError, OSError):
        return False


f = open("data.txt", "w")

print(is_file_descriptor(f))
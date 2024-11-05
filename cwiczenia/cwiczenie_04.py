"""
N x M

     1   2   3

1    1   2   3
2    2   4   6
3    3   6   9

"""

# help(print)
#
# print()
# print(1, 2, 3, 4, sep="-", end=":")
# print(1, 2, 3, 4, sep="-")
# x = 10
# print(f"{x:3}")
#

N = 3
M = 11

print("   ", end="")
for i in range(1, M):
    print(f"{i:4}", end="")

print("\n")

for x in range(1, N):
    print(x, end="  ")
    for y in range(1, M):
        print(f"{x*y:4}", end="")

    print()
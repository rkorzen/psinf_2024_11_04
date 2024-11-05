
"""
0! = 1
5! = 5 * 4! = 5  * 4 * 3! ... = 5 * 4 * 3 * 2 * 1 * 1

"""

def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(0))


def incr(n):
    print(n)
    incr(n+1)
    
incr(1)


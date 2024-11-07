import sys
from kalkulator import exchange

if len(sys.argv) < 3:
    print("Usage: cli2.py <code> <amount>")

code = sys.argv[1]
amount = sys.argv[2]

print(exchange(code, float(amount)))

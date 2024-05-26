from os import getenv
from random import randint
from check import check


FLAG = getenv("FLAG") or "flag"

print('''Find such x: a * x == b (mod m), if x doesn't exist, send "n"''')

for i in range(50):
    a, b, m = randint(1, 100), randint(1, 100), randint(1, 100)
    print(f"{a} {b} {m}")

    if not check(a, b, m, input()):
        print(":^(")
        break

else:
    print(FLAG)

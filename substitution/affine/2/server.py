from os import getenv
from random import randint
from string import ascii_lowercase
from math import gcd


FLAG = getenv("FLAG") or "flag"
alphabet = ascii_lowercase

m = len(alphabet)
a = randint(2, len(alphabet) - 1)
while gcd(a, m) != 1:
    a = randint(2, len(alphabet) - 1)
b = randint(1, len(alphabet) - 1)

print(a, b)
enc = ""
for c in FLAG:
    i = alphabet.index(c)
    enc += alphabet[(a * i + b) % m]
print(enc)

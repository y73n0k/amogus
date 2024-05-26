from os import getenv
from random import choices
from itertools import cycle
from string import ascii_lowercase


FLAG = getenv("FLAG") or "flag"

alphabet = ascii_lowercase

key = "".join(choices(alphabet, k=len(FLAG) // 3))
print(key)

enc = ""
for c, k in zip(FLAG, cycle(key)):
    i = (alphabet.index(c) + alphabet.index(k)) % len(alphabet)
    enc += alphabet[i]
print(enc)

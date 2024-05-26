from os import getenv
from random import shuffle
from string import ascii_lowercase


FLAG = getenv("FLAG") or "flag"
alphabet = ascii_lowercase

table = list(alphabet)
shuffle(table)
table = "".join(table)

print(f"{table = }")

enc = ""
for c in FLAG:
    index = alphabet.index(c)
    enc += table[index]
print(enc)

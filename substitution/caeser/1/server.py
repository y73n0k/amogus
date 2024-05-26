from os import getenv
from random import choices, randint
from caeser import encrypt, alphabet


FLAG = getenv("FLAG") or "flag"

print(f"{alphabet = }")
for i in range(15):
    text = "".join(choices(alphabet, k=10))
    shift = randint(1, len(alphabet) - 1)
    print(text)
    print(shift)
    if input() != encrypt(text, shift):
        print(":^(")
        break
else:
    print(FLAG)

from os import getenv
from random import choices, randint
from caeser import decrypt, alphabet

FLAG = getenv("FLAG") or "test"

print(f"{alphabet = }")
for i in range(15):
    text = "".join(choices(alphabet, k=10))
    shift = randint(1, len(alphabet) - 1)
    print(text)
    print(shift)
    if input() != decrypt(text, shift):
        print(":^(")
        break
else:
    print(FLAG)

from os import getenv
from random import randint
from caeser import encrypt, alphabet

FLAG = getenv("FLAG") or "test"

print(f"{alphabet = }")
shift = randint(1, len(alphabet) - 1)
print(encrypt(FLAG, shift))
print(FLAG[2])

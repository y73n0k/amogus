from os import getenv
from Crypto.Util.number import getStrongPrime
from Crypto.Random.random import randint


def gen():
    q = getStrongPrime(1024)
    g = randint(1,q-1)
    s = randint(1,q-1)
    h = pow(g,s,q)
    return q,g,h


def commit(pk, m):
    q, g, h = pk
    r = randint(1,q-1)
    comm = (pow(g,m,q) * pow(h,r,q)) % q
    return comm,r


def verify(param, c, r, x):
    q, g, h = param
    if not (x > 1 and x < q):
        return False
    return c == (pow(g,x,q) * pow(h,r,q)) % q


def roll_dice(pk):
    roll = randint(1,6)
    comm, r = commit(pk,roll)
    return comm, roll, r


def check_dice(pk,comm,guess,r):
    res = verify(pk,comm, r, int(guess))
    return res


q,g,h = gen()
pk = q,g,h
print(f'public key:\nq = {q}\ng = {g}\nh = {h}')

game = roll_dice
verif = check_dice

correct = 0
for _ in range(256):
    if correct == 250:
        print(f"{getenv("FLAG")}")
        exit()

    comm, _, r = game(pk)
    print(f'Commitment: {comm}')
    guess = input(f'whats your guess?')
    if verif(pk, comm, guess, r):
        correct += 1
        print("Correct!")
    else:
        exit()

print(f'>:3')
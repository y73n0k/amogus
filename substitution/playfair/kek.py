from os import getenv
from string import ascii_lowercase as alphabet


alphabet = list(alphabet)
alphabet.remove('j')

KEY = "amogus"

FLAG = "thgvnskqiqwpdtugdpqyqyqy"

table = KEY
for c in alphabet:
    if c not in KEY:
        table += c

s = FLAG
while True:
    b = [s[i: i + 2] for i in range(0, len(s), 2)]
    for i in range(0, len(b)):
        bb = b[i]
        if len(bb) == 2:
            if bb[0] == bb[1]:
                s = s[:2 * i + 1] + "x" + s[2 * i + 1:]
                break
    else:
        break

if len(s) % 2 == 1:
    s += "x"
b = [s[i: i + 2] for i in range(0, len(s), 2)]

to_coor = lambda x: (x // 5, x % 5)
to_inedx = lambda x, y: x * 5 + y

res = ""
for bb in b:
    a, b = table.index(bb[0]), table.index(bb[1])
    (x1, y1), (x2, y2) = to_coor(a), to_coor(b)
    if x1 == x2:
        res += table[to_inedx(x1, (y1 - 1) % 5)]
        res += table[to_inedx(x2, (y2 - 1) % 5)]
    elif y1 == y2:
        res += table[to_inedx((x1 - 1) % 5, y1)]
        res += table[to_inedx((x2 - 1) % 5, y2)]
    else:
        res += table[to_inedx(x1, y2)]
        res += table[to_inedx(x2, y1)]

print(res)
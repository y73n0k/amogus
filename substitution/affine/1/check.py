from math import gcd


def check(a, b, m, answer):
    if b % gcd(a, m) == 0:
        try:
            return (int(answer) * a) % m == b % m
        except:
            return False
    return answer == "n"

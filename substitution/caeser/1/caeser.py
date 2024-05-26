from string import ascii_lowercase


alphabet = ascii_lowercase


def encrypt(message, shift):
    result = ""
    for c in message:
        result += alphabet[(alphabet.index(c) + shift) % len(alphabet)]
    return result


def decrypt(message, shift):
    return encrypt(message, -shift)

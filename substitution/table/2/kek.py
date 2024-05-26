from Crypto.Util.number import bytes_to_long, long_to_bytes


a = bytes.fromhex("f44862937fef823374c9a212f5af82f3bf0f825e5f68839fba75837f7a757af234483bf25508635f7ea863537e6f9ab3")

sbox = (
        (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
        (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
        (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
        (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
        (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
        (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
        (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
        (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
        )

blocks = [a[i:i+4] for i in range(0, len(a), 4)]

res = b""

for t in blocks:
    kek = bytes_to_long(t)
    kek = ((kek >> (32 - 11)) | (kek << 11)) & 0xFFFFFFFF
    output = 0
    for i in range(8):
        output |= ((sbox[i].index((kek >> (4 * i)) & 0b1111)) << (4 * i))
    res += long_to_bytes(output)
print(res.decode())
 
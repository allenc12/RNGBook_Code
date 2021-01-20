#!/usr/bin/env python3

# A weak RNG with only 16 bit keys
from Crypto.Cipher import AES

key = 0x2984  # 16 bit key.
V = 0x0123456789ABCDEF0123456789ABCDEF  # 128 bit vector


def byteify(n):
    bytelist = list()
    for j in range(16):
        bytelist.append((n >> (8 * j)) & 0xFF)
    return bytes(bytearray(bytelist))


def debyteify(bytelist):
    bi = 0
    for i in range(16):
        bi = (bi << 8) + ord(bytelist[15 - i])
        # print "debyteify  %x" % ord(bytelist[15-i])
    return bi


def printbytes(h, b):
    st = h
    for i in range(16):
        st = st + "%02x" % ord(b[15 - i])
    print(st)


cipher = AES.new(byteify(key), AES.MODE_ECB)
outputs = list()
for i in range(6):
    outputs.append(cipher.encrypt(byteify(V)))
    V += 1

# Now outputs[] contains 6 randomish values
for i in range(len(outputs)):
    print("Output %d : %032x" % (i, debyteify(outputs[i])))

# Now search for the key using first three numbers.
for i in range(65536):
    trialkey = byteify(i)
    cipher = AES.new(trialkey, AES.MODE_ECB)
    try1 = debyteify(cipher.decrypt(outputs[0]))
    try2 = debyteify(cipher.decrypt(outputs[1]))
    try3 = debyteify(cipher.decrypt(outputs[2]))

    if (try3 == (try2 + 1)) and (try2 == (try1 + 1)):
        print("Key %04x works" % i)
        break
# Now predict the next 3 values
predict1 = cipher.encrypt(byteify(try3 + 1))
predict2 = cipher.encrypt(byteify(try3 + 2))
predict3 = cipher.encrypt(byteify(try3 + 3))

print("Prediction for outputs 3-5:")
print("%032x" % debyteify(predict1))
print("%032x" % debyteify(predict2))
print("%032x" % debyteify(predict3))

#!/usr/bin/env python3


def lcg(a, c, m, seed):
    x = seed
    while True:
        x = (x * a + c) % m
        yield (x >> 16) & 0xFFFFFFFF


lcginst = lcg(a=0x5DEECE66D, c=11, m=2 ** 48, seed=0x3A6F9EB64)
for i in range(10):
    print("0x%08x" % next(lcginst))

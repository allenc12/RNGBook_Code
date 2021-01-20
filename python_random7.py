#!/usr/bin/env python

from rdrand import RdRandom

r = RdRandom()
for i in range(5):
    print("%f" % r.random())
print()
for i in range(5):
    print("%032X" % r.getrandbits(256))


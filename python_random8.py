#!/usr/bin/env python3

from rdrand import RdSeedom

r = RdSeedom()
for i in range(5):
    print("%f" % r.random())
print()
for i in range(5):
    print("%032X" % r.getrandbits(256))


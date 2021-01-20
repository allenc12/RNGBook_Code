#!/usr/bin/env python3

import random

r = random

for i in range(1, 17):
    x = r.getrandbits(i)
    print("  bits: %2d random value: 0x%04x" % (i, x))

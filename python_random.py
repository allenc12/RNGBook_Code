#!/usr/bin/env python3

import random

r = random
s = r.getstate()

print("random.random() Returns floating point numbers in [0,1)")
for i in range(3):
    x = r.random()
    print(" ", x)

r.setstate(s)

print("Reseeding with the starting state causes it to repeat")
for i in range(3):
    x = r.random()
    print(" ", x)

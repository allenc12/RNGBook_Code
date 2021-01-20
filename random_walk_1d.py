#!/usr/bin/env python3

import random

repetitions = 10000
steps = 30
finalstates = [0 for i in range(0, steps + 1)]
for i in range(repetitions):
    state = 0
    for j in range(steps):
        if random.choice([True, False]):
            state += 1
        else:
            state -= 1
    finalstates[abs(state)] += 1
# Print out
for i in range(0, steps + 1):
    print("%d %d" % (i, finalstates[i]))

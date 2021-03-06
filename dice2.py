#!/usr/bin/env python3

import sys, random

randsource = random.SystemRandom()  # nondeterministic random source

sides = int(sys.argv[1])
number_of_rolls = int(sys.argv[2])
throws = [randsource.randint(0, sides - 1) for x in range(number_of_rolls)]
for throw in throws:
    print(throw)

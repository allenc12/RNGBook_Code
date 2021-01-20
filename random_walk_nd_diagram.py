#!/usr/bin/env python3

import sys
import random
import math

n = 2  # 2 dimension
steps = int(sys.argv[1])  # Number of steps
number_of_paths = int(sys.argv[2])  # number of paths
filename = sys.argv[3]  # filename prefix for the data files


def random_unit_n_vector(n):
    v = [random.gauss(0, 1) for i in range(n)]
    m = math.sqrt(sum(x * x for x in v))
    return [x / m for x in v]


for i in range(number_of_paths):
    path = list()
    state = [0.0 for x in range(n)]
    path.append(state)
    for j in range(steps):
        step = random_unit_n_vector(n)
        state2 = [a + b for a, b in zip(state, step)]
        state = state2
        distance = math.sqrt(sum(x * x for x in state))
        path.append(state)

    thefile = open(filename + "_%d.dat" % i, "w")
    for point in path:
        line = str(point[0]) + "  " + str(point[1]) + "\n"
        thefile.write(line)
    thefile.close()

#!/usr/bin/env python3

import sys
import random
import math
from fractions import gcd
rs = random.SystemRandom()

coprime = 0
n = int(sys.argv[1])

for i in range(n):
    a = rs.getrandbits(64)
    b = rs.getrandbits(64)
    if (gcd(a,b)==1):
        coprime += 1; 

pi_approx = math.sqrt((6.0*n)/coprime)
err = (abs(math.pi - pi_approx)/math.pi)*100.0
print("Pi approximately = %8.6f  Error = %8.6f%%" % (pi_approx, err))

 
    

#!/usr/bin/env python3
#!/usr/bin/env python3

import random

r = random.SystemRandom()

for i in range(5):
    key = r.getrandbits(256)
    print("  %064x" % key)

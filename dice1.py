import sys, random

randsource = random.SystemRandom()  # nondeterministic random source

throws = [randsource.randint(1, 6) for x in range(18)]
print(throws)

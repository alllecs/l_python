import itertools
import math

def primes():
    i = 2
    while True:
        if (math.factorial(i - 1) + 1) % i == 0:
#        if i == 2 or i == 3 or i > 3 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            yield i
        i += 1
#primes()
print(list(itertools.takewhile(lambda x : x <= 99, primes())))

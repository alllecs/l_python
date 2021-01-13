#!/usr/bin/python3

import math

def ann(s, n, k):
    ka = k / 1200
    return (ka * (1 + ka) ** n) / ((1 + ka) ** n - 1) * s

s = int(input())
n = int(input())
k = int(input())
d = 0
a = 0
dn = 0
an = 0

for t in range(n):
    dn = s / n + (s - (t) * s / n) * k / 1200
    an = ann(s, n, k)
    d += dn
    a += an
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t + 1, dn, an))

print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (d - s, a - s))


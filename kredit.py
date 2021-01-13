#!/usr/bin/python3

import math

def compute_payment(t, s, n, k):
    p = s / n + (s - (t - 1) * (s / n)) * (k / (12 * 100))
    return p

s = int(input())
n = int(input())
k = int(input())
x = 0

for t in range(1, n + 1):
    p = compute_payment(t, s, n, k)
    x += p
    print("%2d месяц - %8.2f руб" % (t,  p))
x = x - s
print("Доход банка - %6.2f руб" % x)


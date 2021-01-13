#!/usr/bin/python3


import math

def compute_population(t):
    c = 172
    t1 = 2000
    tay = 45
    n = c / tay * (math.pi / 2 - math.atan((t1 - t) / tay))
    return n

line = input()

years_str_list = line.split()

n = len(years_str_list)

years_list = [int(a) for a in years_str_list]
population_list = [compute_population(b) for b in years_list]

for c in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[c], population_list[c]))



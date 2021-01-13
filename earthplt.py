#!/usr/bin/python3

import math
#import matplotlib.pyplot as plt

x_list = [1, 5, -3]
y_list = [-5, 6, 1 ]

def compute_population(t):
    c = 172
    t1 = 2000
    tay = 45
    n = c / tay * (math.pi / 2 - math.atan((t1 - t) / tay))
    print(n)
    return n

#line = input()

#years_str_list = line.split()


years_list = [i for i in range(1000, 3000)]
n = len(years_list)
population_list = [compute_population(b) for b in years_list]
for c in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[c], population_list[c]))

#line = plt.plot(years_list, population_list)
# Позиция zero
#plt.gca().spines["left"].set_position("zero")
#plt.gca().spines["bottom"].set_position("zero")

#plt.show()


#!/usr/bin/python3

import math

def compute_lambda(t):
    b = 33
    l_0 = 884
    t_0 = 100
    y = b * l_0 / (t - t_0)
    return y

t1 = float(input("t1 = "))
t2 = float(input("t2 = "))

if t2 <= t1 or t1 <= 100:
    print("Неверные границы температур")
else:
    n = 20
    h = (t2 - t1) / (n - 1)
    t_list = [t1 + i * h for i in range(0,n)]
    lambda_list = [compute_lambda(t) for t in t_list]
    print("-" * 21)
    print("| %7s | %7s |" % ("t", "L(t)"))
    print("-" * 21)
    for i in range(len(t_list)):
        print("| %7.2f | %7.2f |" % (t_list[i], lambda_list[i]))
    print("-" * 21)


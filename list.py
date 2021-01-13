#!/usr/bin/python3
from math import *

#line = input()
#str_list = line.split()

#x_list = [float(x) for x in str_list]
#print(x_list)

def f_x(x):
    try:
        y = 1 / (x+1) + x / (x-3)
    except:
        y = math.inf
    return y




#!/usr/bin/python3

import  numpy as np

def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y

x_array = list(map(float, input().split()))
h_array = list(map(float, input().split()))
ox = float(input())
oy = float(input())

# Движение снаряда
a = np.polyfit(x_array, h_array, 2)

#Расположение пушки
h_zero = get_trend(0, a)

#print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

h_target = get_trend(ox, a)

delta_h = abs(oy - h_target)

if delta_h <= 0.5:
    print("h0 = %6.2f, %2s" % (h_zero, "yes"))
else:
    print("h0 = %6.2f, %2s" % (h_zero, "no"))


#!/usr/bin/python3


import math
import matplotlib.pyplot as plt

def f_x(x):
#    y = x ** 3 - 6 * x ** 2 +  x + 5
    y = math.exp(math.cos(math.radians(x))) + math.log(math.sin(0.8 * math.radians(x)) ** 2 + 1) * math.cos(math.radians(x))
    return y

def y_x(x):
#    y = (x - 2) ** 2 -6
    y = -math.log((math.cos(math.radians(x)) * math.sin(math.radians(x))) ** 2 + 1.7) + 2
    return y

x_list = [i for i in range(-240, 360)]
f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]

line_f = plt.plot(x_list, f_list, label='f(x)')
line_y = plt.plot(x_list, y_list, label='y(x)')

plt.setp(line_f, color="blue", linewidth=2)

plt.setp(line_y, color="red", linewidth=2)
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.legend()
plt.title("Графики функций")
plt.show()

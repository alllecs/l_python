#!/usr/bin/python3

from math import *

def compute_len(x_0, y_0, x_1, y_1):
    len = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len

def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area

def compute_angle(a_1, a_2, a_3):
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2) / (2 * a_1 * a_2))
    return degrees(angle_rad)

def rad_in(a, b, c, p):
    r = sqrt(((p / 2 - a) * (p / 2 - b) * (p / 2 - c)) * 2 / p )
    return r

def rad_out(a, b, c, s):
    r = (a * b * c) / (4 * s)
    return r

x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)
p = a + b + c
s = compute_area(a, b, c)

if a + b <= c or b + c <= a or a +c <= b:
    print("Треугольник не существует")
else:
    m_a = 1 / 2 * sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
    m_b = 1 / 2 * sqrt(2 * (a ** 2 + c ** 2) - b ** 2)
    m_c = 1 / 2 * sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
    r_in = rad_in(a, b, c, p)
    r_out = rad_out(a, b, c, s)
    su_m = m_a + m_b + m_c

    print("Радиус вписанной: ", r_in)
    print("Радиус описанной: ", r_out)
    print("Сумма длин медиан: ", su_m)

from math import *

h = int(input())
m = int(input())
s = int(input())

if (0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <= 59):
    angle = 360 / 12 * h + m * 0.5 + s / 120
    print(round(angle, 2))
else:
    print("error")

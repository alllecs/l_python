#!/usr/bin/python3

import math

consum = list(map(int, input().split()))
month = int(input())
norm = float(input())
snorm = float(input())
cost = 0
year = 0

for i in range(len(consum)):
    if (consum[i] > month):
        cost += (consum[i] - (consum[i] - month)) * norm + (consum[i] - month) * snorm
    else:
        cost += consum[i] * norm
    year += consum[i] 
print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (year, cost))



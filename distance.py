#!/usr/bin/python3

import math

def compute_distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

x = list(map(int, input().split()))
y = list(map(int, input().split()))
k = int(input())
r = int(input())
distances = []

#distances = [((x[i] - x[k]) ** 2 + (y[i] - y[k]) ** 2) ** .5 for i in range(len(x))]
for i in range(len(x)):
    distances.append(compute_distance(x[i], y[i], x[k], y[k]))

count = 0
for d in distances:
    if (d <= r):
        count = count + 1
print(count)



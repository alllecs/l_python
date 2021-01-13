#!/usr/bin/python3

import numpy as np

path = list(map(int, input().split()))
speed = list(map(int, input().split()))
num_in = int(input())
num_out = int(input()) + 1

path_n = path[num_in:num_out]
speed_n = speed[num_in:num_out]

len_path = np.sum(path[num_in:num_out])
#print("Расстояние между пунктами А и В :", len_path)

time = []
sum_time = 0
for i in range(len(path_n)):
    time.append(path_n[i] / speed_n[i])
    sum_time += time[i]
#time = path[num_in:num_out] / speed[num_in:num_out]
#sum_time = time.sum()
#print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time
#print("Средняя скорость : ", round(avg_speed, 2))
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, round(sum_time, 2),  round(avg_speed, 2)))

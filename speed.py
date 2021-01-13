#!/usr/bin/python3

import numpy as np

#path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5])
#speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])

line_p = input()
list_p = line_p.split()
path = np.array(list_p, dtype = int)
line_s = input()
list_s = line_s.split()
speed= np.array(list_s, dtype = int)

len_path = np.sum(path)
#print("Расстояние между пунктами А и В :", len_path)

time = path / speed
sum_time = time.sum()
#print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time
#print("Средняя скорость : ", round(avg_speed, 2))
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, round(sum_time, 2),  round(avg_speed, 2)))

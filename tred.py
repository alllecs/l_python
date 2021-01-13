#!/usr/bin/python3

import  numpy as np

month = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11])

temperature = np.array([4, 8, 14, 19, 23, 27, 29, 28, 25, 18, 11, 6])

k_poly = np.polyfit(month, temperature, 2)

print(k_poly)

#!/usr/bin/python3

import math

def compute_lambda(t):
    c = 172
    t1 = 2000
    tay = 45
    n = c / tay * (math.pi / 2 - math.atan((t1 - t) / tay))
    return n

x = int(input())
y = int(input())
y = y + 1

years = [1000, 1750, 1800, 1850, 1900, 1950, 
        1955, 1960, 1965, 1970, 1975, 1980, 1985,
        1990, 1995, 2000, 2005, 2010, 2011, 2012,
        2013, 2014, 2015, 2016, 2017, 2018, 2019]
years = years[x:y]
population = [0.400, 0.791, 1.000, 1.262, 1.650, 2.519, 
        2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
        5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
        7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]
population = population[x:y]

lambda_list = [compute_lambda(t) for t in years]

#error_list = [abs((population[i] - lambda_list[i]) /  lambda_list[i]) for i in range(len(years))]
#error_list = [abs((lambda_list[i] - population[i]) / lambda_list[i]) for i in range(len(years))]
#error_list = [abs((population[i] - lambda_list[i]) / population[i] ) for i in range(len(years))]
error_list = [abs((population[i] - lambda_list[i]) / population[i] ) for i in range(len(years))]

for i in range(len(error_list)):
    print("| %4d | %7.3f | %7.3f | % 7.3f " % (years[i], lambda_list[i], population[i], error_list[i] ))

max_error = max(error_list)
index_max_error = error_list.index(max_error)
min_error = min(error_list)
index_min_error = error_list.index(min_error)
avg_error = sum(error_list) / len(years)
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f" % (years[index_min_error], years[index_max_error], (avg_error * 100)))

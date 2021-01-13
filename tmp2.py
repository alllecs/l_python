#!/usr/bin/python3

from math import atan, pi

def population_t(t):
    N = 172/45*(pi/2-atan((2000-t)/45))
    return N

t1 = int(input())

t_2 = int(input())

t2 = t_2+1

years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 
                 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
                          2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
                                   2016, 2017, 2018, 2019]

p =[0.400,0.791,1.000,1.262,1.650,2.519,
                     2.756,3.021,3.335,3.692,4.068,4.435,4.831,
                                  5.264,5.674,6.071,6.344,6.933, 7.015,7.100,
                                               7.162,7.271,7.358,7.444,7.530,7.669,7.763]

t_p = [population_t(years[i]) for i in range(len(years[t1:t2]))]

error_list = [abs((p[k]-t_p[k])/p[k]) for k in range(t1, t2)]

max_y = years[error_list.index(max(error_list))]

min_y = years[error_list.index(min(error_list))]

avr_error = sum(error_list)/len(error_list)

print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"%(min_y, max_y, avr_error*100))

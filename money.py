#!/usr/bin/python3
from math import *

# deposit - сумма вклада, interest_rate -процентная ставка,
# # amount_months - количество месяцев
#
def compute_income(deposit, interest_rate, amount_months):
    z = deposit * (1 + interest_rate / (12 * 100)) ** amount_months
    return z

k = 7.0 #float(input()) #процент вклада
n = 8 #int(input()) #количество месяцев
s = 549 # float(input()) # прибыль

for x in range(1000, 30000):
    income = compute_income(x, k, n) - x
    if round(income) == s:
        print("%d" % x) 

from math import *

#Посчитать, сколько банок краски необходимо, чтобы окрасить внутреннюю площадь бассейна кубической формы со стороной а метров, если расход краски на 1 квадратный метр  составляет b миллилитров, а в банке содержится v литров краски.

a = float(input())
b = float(input())
v = int(input())

if a > 0 and b > 0 and v > 0:
    ob = 5 * a ** 2
    ras = b * ob
    l = ceil(ras / (v * 1000))
    print(l)
else:
    print("error")
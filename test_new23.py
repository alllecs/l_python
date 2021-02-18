"""
Find string a in string s and replace it with b
"""

s = str(input())
a = str(input())
b = str(input())
n = 0
while a in s:
    s = s.replace(a, b)
    n += 1
    if n >= 1000:
        break
if n >= 1000:
    print("Impossible")
else:
    print(n)

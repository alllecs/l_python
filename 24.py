#!/usr/bin/python3

t1 = list(input().split())
#line = input().split()
#l_list = [float(t) for t in line]
t2 = list(input().split())
mt = float(input())

for i in range(len(t1)):
    t = (float(t1[i]) + float(t2[i])) / 2 
    if t > mt:
        print(i)



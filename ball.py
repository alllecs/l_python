#!/usr/bin/python3

n = int(input())
match = []
stat = {}

win = [1, 1, 0, 0, 3]
los = [1, 0, 0, 1, 0]
non = [1, 0, 1, 0, 1]

for i in range(n):
    match = input().split(";")
    if match[0] not in stat:
        stat[match[0]] = [0, 0, 0, 0, 0]
    if match[2] not in stat:
        stat[match[2]] = [0, 0, 0, 0, 0]
    if int(match[1]) > int(match[3]):
        stat[match[0]] = [stat[match[0]] + win for stat[match[0]], win in zip( stat[match[0]], win)]
        stat[match[2]] = [stat[match[2]] + los for stat[match[2]], los in zip( stat[match[2]], los)]
    elif int(match[1]) < int(match[3]):
        stat[match[2]] = [stat[match[2]] + win for stat[match[2]], win in zip( stat[match[2]], win)]
        stat[match[0]] = [stat[match[0]] + los for stat[match[0]], los in zip( stat[match[0]], los)]
    else:
        stat[match[0]] = [stat[match[0]] + non for stat[match[0]], non in zip( stat[match[0]], non)]
        stat[match[2]] = [stat[match[2]] + non for stat[match[2]], non in zip( stat[match[2]], non)]
for key in stat.keys():
    print("%s:" % key, end="")
    for i in range(len(stat[key])):
        print(stat[key][i], end=' ')
    print()



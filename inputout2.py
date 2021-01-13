#!/usr/bin/python3


dic = []
mat, p, rus = 0, 0, 0
with open("data.txt", "r") as f:
    for line in f:
        dic.append(line.lower().strip().split(";"))

for i in range(0, len(dic)):
    print((int(dic[i][1]) + int(dic[i][2]) + int(dic[i][3])) / 3)
    mat += int(dic[i][1])
    p += int(dic[i][2])
    rus += int(dic[i][3])

print(mat / len(dic), p / len(dic), rus / len(dic))




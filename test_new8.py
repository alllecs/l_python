import sys
#sys.stdin = open("input4.txt", "r")
#2
#A : C B
#B : D E
#1
#E A
#Yes


def ye(c, p):
    if not parent[p] and c != p:
#        print("No")
        return "No"
    if c == p or c in parent[p]:
#        print("Yes")
        return "Yes"
    else:
#        n = ""
#        print(parent, c, p)
        x = "No"
        for i in parent[p]:
            if (i in parent):
                x = ye(c, i)
                if x == "Yes":
                    break
#            n = ye(c, i)
        return x

parent = {}
num = int(input())

for i in range(0, num):
    line = input().split()
    if len(line) > 2 :
        del line[1]
        c = line.pop(0)
        if not c in parent:
            parent[c] = []
        parent[c].extend(line)
    else: parent[line[0]] = []

num = int(input())
for i in range(0, num):
    line = input().split()
    if len(line) < 2:
        print("No")
    elif line[0] == line[1]:
        print("Yes")
    elif line[1] in parent:
        res = ye(line[0], line[1])
        print(res)
    else:
        print("No")

import sys
#sys.stdin = open("input11t.txt", "r")
sys.stdin = open("input11t2.txt", "r") # 5 10 1 3 2 8 7 
#sys.stdin = open("input11t3.txt", "r") # z w z

def is_parent(child):
    x = False
    if child in parents:
        for i in parents[child]:
            if i in arr:
                return True
            else:
                x = is_parent(i)
                if x: return x
    return x

n = int(input())

parents = {}
arr = []

for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]


n = int(input())
for _ in range(n):
    a = input()
    if is_parent(a): print(a)
    arr.append(a)

a = [int(i) for i in input().split()]
for i in range(max(a) + 1):
    if a.count(i) > 1:
        print(i, end=' ')

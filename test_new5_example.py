#dic = {'global': {'parent': None, 'variables': set()}}
dic = {'global' : set()}
n = int(input())

for i in range(0, n):
    line = list(map(str, input().split()))
    print(dic)
    dic['global'].add(line[1])
    print(dic)




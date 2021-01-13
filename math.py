m = []
while True:
    l = input()
    if l == 'end':
        break
    m += [[int(i) for i in l.split()]]

row = len(m)
col = len(m[0])

for i in range(row):
    for j in range(col):
        n = m[i + 1 - row][j] + m[i][j - 1] + m[i - 1][j] + m[i][j + 1 - col]
        print(n, end=' ')
    print()

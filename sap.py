n, m = list(map(int, input().split()))
field = [input() for x in range(n)]
num_field = []

def check_append(c_i, c_j):
    if c_i >= 0 and c_i < len(num_field) and c_j >= 0 and c_j < len(num_field[c_i]):
        if num_field[c_i][c_j] != '*':
            num_field[c_i][c_j] += 1

for i in range(len(field)):
    num_field.append(list(field[i]))
    for j in range(len(field[i])):
            if field[i][j] == '.':
                num_field[i][j] = 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '*':
            check_append(i, j + 1)
            check_append(i, j - 1)
            check_append(i - 1, j + 1)
            check_append(i - 1, j)
            check_append(i - 1, j - 1)
            check_append(i + 1, j + 1)
            check_append(i + 1, j)
            check_append(i + 1, j - 1)

for i in range(len(num_field)):
    num_field[i] = list(map(str, num_field[i]))
    print("".join(num_field[i]))

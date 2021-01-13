line = []
with open('dataset.txt') as f:
    for i in f.readline().strip():
        line.append(i)

for i in range(len(line)):
    if str.isdigit(line[i]) and str.isdigit(line[i + 1 - len(line)]):
        line[i] = line[i] + line[i + 1 - len(line)]

for i in range(len(line)):
    if str.isdigit(line[i]) and not str.isdigit(line[i - 1]):
        for j in range(int(line[i])):
                print(line[i - 1], end='')
print()

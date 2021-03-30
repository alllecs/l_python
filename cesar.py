hift, line = int(input()), input().strip()
alf = ' abcdefghijklmnopqrstuvwxyz'
new_line = ""
for i in range(len(line)):
    new_line += alf[(alf.find(line[i]) + shift) % len(alf)]
print("Result: \"" + new_line+ "\"")

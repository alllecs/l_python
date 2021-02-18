s = str(input())
t = str(input())
n = 0
#print(sum(1 for i in range(len(s)) if s.startswith(t, i)))
for i in range(len(s) - len(t) + 1):
#    if s[i:len(t) + i].find(t) == 0:
    if s[i:].startswith(t):
        n += 1
print(n)

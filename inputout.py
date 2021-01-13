#!/usr/bin/python3

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

dic = []
sor = {}
line = ''

with open('data.txt') as f:
    for i in f:
        line = line + i

dic = line.lower().split()
for i in dic:
    sor[i] = dic.count(i)
max_v = max(sor.values())
print(get_key(sor, max_v), max_v)


#NEXT GEN
s, d, m, w = str(), dict(), 0, str()
with open("data.txt", "r") as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word
print(w, d[w])




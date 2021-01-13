#!/usr/bin/python3

d = int(input())
know_words = []
new_words = []

for i in range(0, d):
    know_words.append(str(input().lower()))


l = int(input())
for i in range(0, l):
    new_words.append(list(map(str, input().lower().split())))

for i in range(0, len(new_words)):
    for j in range(0, len(new_words[i])):
        if not new_words[i][j] in know_words:
            print(new_words[i][j])
            know_words.append(new_words[i][j])




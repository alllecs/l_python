import json

def dfs(p1, c1):
    for n in sort_parent[c1]:
        if not n in sort_parent[p1]:
            sort_parent[p1].append(n)
        dfs(p1, n)

#temp = json.loads(input())
with open("input_file.json") as jf:
    temp = json.load(jf)

parent = dict()
sort_parent = dict()
child = []
for j in range(len(temp)):
    parent[temp[j]['name']] = [i for i in temp[j]['parents']]


for i in parent.keys():
    sort_parent[i] = []
    for j in parent.keys():
        if i in parent[j]:
            sort_parent[i].append(j)

print(sort_parent)
for i in sort_parent.keys():
    dfs(i, i)
    child.append(i)
    
child.sort()
for i in child:
    print(i, ":", len(sort_parent[i]) + 1)

"""
def test(x, c):
    for i in z:
        if x in i['parents']:
            c.add(i['name'])
            c = test(i['name'], c)
    return c

z = json.loads(input())
z.sort(key=(lambda x: x['name']))
for i in z:
    print(i['name'], ':', len(test(i['name'], c = set()))+ 1)
"""

def add(name, var):
    space[name]['variables'].append(var)

def create(name, parent):
    space[name] = {'parent' : parent, 'variables' : []}

def get(name, var):
    if var in space[name]['variables']:
        result.append(name)
    else:
        if space[name]['parent'] == None:
            result.append(None)
        else:
            get(space[name]['parent'], var)

space = {
        'global' : {
            'variables' : [],
            'parent' : None
            }
        }
#space['global']['variables'].append("a")
#space['foo'] = {'variables' : set()}
#space['foo']['variables'].append("b")
#
#

result = []
res = ""

num = int(input())
for i in range(0, num):
    line = list(map(str, input().split()))
    if line[0] == "create":
        create(line[1], line[2])
    elif line[0] == "add":
        add(line[1], line[2])
    elif line[0] == "get":
        get(line[1], line[2])

for i in range(0, len(result)):
    print(result[i])

#Example generator

{ord(x) for x in 'spaam'}    # генерируем set {112, 115, 109, 97}

{x:ord(x) for x in 'spaam'}  # генерируем dictionary {'s': 115, 'm': 109, 'p': 112, 'a': 97}

x = [-2, -1, 0, 1, 2]
y = []
for i in x:
    y.append(i * i)
print(y)
y = [i * i for i in x]
print(y)
y = [i * i for i in x if i > 0]
print(y)

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)
z = []
for x in range(3):
    for y in range(3):
        if y >= x:
            z.append((x, y))
print(z)
z = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(z) #generator object <genexpr>


#[1, 2, 3, 4]
a = [i + 1 for i in range(4)]
a = [i for i in range(5)][1:]
a - list(i + 1 for i in range(4))

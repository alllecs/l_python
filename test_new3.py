def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return ((x + 5 - 1) // 5) * 5


def closest_mod_5_2(x):
    if x % 5 == 0:
        return x
    for i in range(1, 5):
        if (x + i) % 5 == 0:
            return x + i

for i in range(1, 10):
    print(closest_mod_5_2(i))

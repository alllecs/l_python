def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key * 2 in d:
        d[key * 2] += [value]
    else:
        d[key * 2] = [value]

x = {}
print(update_dictionary(x, 0, -5))
print(x)
update_dictionary(x, 1, -1)
print(x)
update_dictionary(x, 2, -2)
print(x)
update_dictionary(x, 3, -3)
print(x)

def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            del l[i]
lst = [1, 2, 3, 4, 5, 6]
print(lst)
modify_list(lst)
print(lst) 

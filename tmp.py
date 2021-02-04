objects = [1, 2, 1, 2, 3]
new_obj = []
ans = 0
for obj in objects: # доступная переменная objects
    if not obj in new_obj: 
        ans += 1
        new_obj.append(obj)
#p[id(obj)] = id(obj)



print(ans)

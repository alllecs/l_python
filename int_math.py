import operator

dic_oper = {
        "plus": operator.add,
        "minus": operator.sub,
        "multiply": operator.mul,
        "divide": operator.floordiv
        }
x1, oper, x2 = input().split()
print(dic_oper[oper](int(x1), int(x2)))

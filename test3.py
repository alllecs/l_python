typ = str(input())
if typ == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif typ == "круг":
    r = float(input())
    s =float(3.14 * r ** 2)
    print(s)
elif typ == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    s = float((p *(p - a)(p - b)(p - c)) ** 0.5)
    print(s)

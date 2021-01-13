#!/usr/bin/python3

x = float(input())
y = float(input())
z = str(input())

if (z == "mod" or z == "/" or z == "div") and y == 0:
    print("Деление на 0!")
elif z == "+":
    print(x + y);
elif z == "-":
    print(x - y);
elif z == "/":
    print(x / y);
elif z == "*":
    print(x * y);
elif z == "mod":
    print(x % y);
elif z == "pow":
    print(x ** y);
elif z == "div":
    print(x // y);
    


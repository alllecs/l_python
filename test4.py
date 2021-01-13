n = int(input())

if n % 10 == 0 or n % 10 >= 5 or (n % 100) // 10 == 1:
    print("%d программистов" % n)
elif n % 10 == 1 and n % 100 != 11:
    print("%d программист" %n)
elif n % 10 >= 2 and n % 100 != 12:
    print("%d программистa" %n)
else:
    print("%d программистов" % n)

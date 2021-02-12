import datetime

y, m, d = map(int, input().split())
delta = int(input())
date = datetime.date(y, m, d) + datetime.timedelta(delta)
print(date.year, date.month, date.day)

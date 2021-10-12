import datetime

dt = datetime.datetime(2020, 11, 4, 14,53,00)
# print(dt)

format = dt.strftime("%Y/%m/%d %H:%M:%S")
print(format)
format = dt.strftime("%Y/%B/%d %H:%M:%S %p")
print(format)
format = dt.strftime("%a, %Y %b %d")
print(format)
format = dt.strftime("%A, %Y %B %d")
print(format)
format = dt.strftime("Weekday: %w")
print(format)
format = dt.strftime("Day of the year: %j")
print(format)
format = dt.strftime("Week number of the year: %W")
print(format)

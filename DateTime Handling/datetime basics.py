import datetime as dt

'''set datetime object to now'''
dt1 = dt.datetime.now()

'''set a datetime object specifiying y,m,d'''
dt2 = dt.datetime(2021, 1, 1)

'''
create delta object using 2 datetime objects.
default format is days, hours/min/sec/ms
'''
dt3 = dt1 - dt2

'''prints delta object using only days property (eliminates time)'''
print(dt3.days)

'''adding to a datetime object using a delta'''
delta = dt.timedelta(days = 1)
print(dt1 + delta)


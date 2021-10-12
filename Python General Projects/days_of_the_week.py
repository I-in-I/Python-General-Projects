class WeekDayError(Exception):
    pass
	

class Weeker:
    
    def __init__(self, day):
        self.__day = day
        self.__week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if self.__day not in self.__week:
            raise WeekDayError
        self.__index = self.__week.index(self.__day)


    def __str__(self):
        return self.__week[self.__index]


    def add_days(self, n):
        n %= 6
        self.__index += n
        

    def subtract_days(self, n):
        n %= 6
        self.__index -= n


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")


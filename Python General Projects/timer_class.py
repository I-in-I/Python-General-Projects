class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def __str__(self):
        hours, minutes, seconds = "", "", ""
        if self.__hours < 10:
            hours = "0" + str(self.__hours)
        else:
            hours = str(self.__hours)
        if self.__minutes < 10:
            minutes = "0" + str(self.__minutes)
        else:
            minutes = str(self.__minutes)
        if self.__seconds < 10:
            seconds = "0" + str(self.__seconds)
        else:
            seconds = str(self.__seconds)
        return f'{hours}:{minutes}:{seconds}'
    

    def next_second(self):
        self.__seconds += 1
        self.time_adjust()
        
        
    def prev_second(self):
        self.__seconds -= 1
        self.time_adjust()
        

    def time_adjust(self):
        if self.__seconds > 59:
            self.__minutes += 1
            self.__seconds = 0
        if self.__minutes > 59:
            self.__hours += 1
            self.__minutes = 0
        if self.__hours > 23:
            self.__hours = 0

        if self.__seconds < 0:
            self.__minutes -= 1
            self.__seconds = 59
        if self.__minutes < 0:
            self.__hours -= 1
            self.__minutes = 59
        if self.__hours < 0:
            self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

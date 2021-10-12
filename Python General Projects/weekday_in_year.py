from calendar import Calendar


'''
"weekday_in_year" is an extension of Calendar class from the calendar module.
It's purpose is to count how many times a given weekday occurs in a year.
'''


class MyCalendar(Calendar):
    def __init__(self, year, weekday):
        Calendar.__init__(self, year)

        self.year = year
        self.weekday = weekday


    def get_weekdays_in_year(self):
        '''
        Given the specified year, generates tuples inside lists for
        for every week of that year.
        See calendar module>Calendar class>monthdays2calendar() function for
        details on its operations, parameters, and formatting.
        '''
        lists = []
        for i in range(1, 13):
            lists.append(Calendar.monthdays2calendar(self, year, i))
##        print(lists)
        return lists
        

    def count_weekday_in_year(self, lists, weekday):
        '''
        Counts all occurences of the given weekday using the tuples
        second position (index[1]) from the get_weekdays_in_year() function.
        Ignores any tuples with 0 in position 0 (index[0]).
        '''
        weekday_count = 0
        for second_layer in lists:
            for single_list in second_layer:
                for tupl in single_list:
                    if tupl[0] != 0 and tupl[1] == weekday:
                        weekday_count += 1
                        
        print(weekday_count)


def get_year():
    '''
    Asks user to input year and validates it
    '''
    flag = False
    year = ''
    
    while flag == False:
        year = input("Enter year as an integer:" )

        if year.isnumeric():
            year = int(year)
            
        if isinstance(year, int):
            flag = True
            break
        else:
            flag = False
            print("Invalid input. Try again.")
            continue
    return year


def get_weekday():
    '''
    Asks user to input full weekday name, formats to uppercase, and
    validates it.
    '''
    flag = False
    weekday = ''
    list_of_weekday_names = ["MONDAY","TUESDAY","WEDNESDAY",\
                             "THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
    
    while flag == False:
        weekday = input("Enter full name of weekday. Example('Sunday'): ")

        if weekday.isalpha():
            weekday = weekday.upper()
            if weekday in list_of_weekday_names:
                flag = True
                break
            else:
                flag = False
                print("Invalid input. Try again.")
                continue
    return weekday


def convert_weekday_to_int():
    '''
    Converts full weekday names to their integer representations.
    0-Monday to 6-Sunday.
    This integer is used in the count_weekday_in_year() function in the
    MyCalendar class.
    '''
    weekday = get_weekday()
    
    if weekday == "SUNDAY":
        weekday = 6
    elif weekday == "SATURDAY":
        weekday = 5
    elif weekday == "FRIDAY":
        weekday = 4
    elif weekday == "THURSDAY":
        weekday = 3
    elif weekday == "WEDNESDAY":
        weekday = 2
    elif weekday == "TUESDAY":
        weekday = 1
    elif weekday == "MONDAY":
        weekday = 0

    return weekday
        

year = get_year()
weekday = convert_weekday_to_int()
mycal = MyCalendar(year, weekday)
lists = mycal.get_weekdays_in_year()


mycal.count_weekday_in_year(lists, weekday)

##tup_list = mycal.monthdays2calendar(year, month)
##print(tup_list)








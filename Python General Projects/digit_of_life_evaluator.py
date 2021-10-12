#digit_of_life_evaluator

#input birthday (all together)
birthday_string = input("Enter Birthday in MMDDYYYY\n\
(all together, no spaces or extra characters): ")

#loop through string, converting to int and sum all int
birthday_int = 0
for char in birthday_string:
    birthday_int += int(char)


#if sum of all int > 9 sum again
if birthday_int > 9:
    birthday_int2 = 0
    birthday_string2 = str(birthday_int)
    for char in birthday_string2:
        birthday_int2 += int(char)
    print(birthday_int2)
else:
    print(birthday_int)

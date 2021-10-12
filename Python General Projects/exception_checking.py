def read_int(prompt, min, max):
    valid = False
    
    while valid == False:
        try:
            number = int(input(prompt))
            assert min < number
            assert number < max
            valid = True
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print(f'Error: the value is not within the permitted range {min}..{max}')
    
    
    if valid == True:
        return number


v = read_int("Enter a number from -10 to 10: ", -10, 10)




print("The number is:", v)

#sudoku takes a 9x9 user-entered list of numbers and checks if there are any
#repeat numbers in any rows, columns or subgrids.
#Sudoku if no duplicates, Not Sudoku if there are duplicates.


def input_validator():
    # Validates user input, making sure only digits from 1-9 are used
    # and that the user has entered sufficient (9) digits.
    # Continues to request input until conditions are met, flag is set to true,
    # and returns input.

    valid = False

    while valid == False:
        input_x = input("Enter 9 digits: ")

        if len(input_x) < 9:
            print("Insufficient digits.")

        if len(input_x) > 9:
            print("Too many digits.")
            
        if input_x.isnumeric() == False:
            print("Non-numeric characters detected.")

        if '0' in input_x:
            print("Do not use zeroes.")

        else:
            valid = True
            return input_x


def list_maker():
    # Converts string to list by taking the user inputted string from
    # input_validator(),
    # and looping through each character - appending it to a list

    input_x = input_validator()
    list_x = []

    for item in input_x:
        list_x += item

    return list_x


def matrix_maker():
    # Creates a bi-dimensional matrix by appending all lists from
    # list_maker() into the list matrix, which is then returned,
    # and stored in a variable "matrix" when this function is called.
    # The while loop calls list_maker() 9 times,
    # enough for 9 lists, to make a 9x9 grid.

    count = 0
    matrix = []

    while count < 9:
        list_x = list_maker()
        count += 1
        matrix.append(list_x)


    return matrix


def horizontal_check():
    # Loops through all lists in matrix and then all numbers in those lists
    # appending new numnbers to duplicates. If a number already exisits in
    # duplicates False is returned. Otherwise if duplicates reaches 9 digits
    # with no repeating numbers, the list duplicates is flushed.

    duplicates = []

    for list_x in matrix:
        for number in list_x:
            
            if len(duplicates) == 9:
                duplicates = []

            if number in duplicates:
                #print("NOT SUDOKU (row)")
                #print(list_x)
                #print()
                return False
                
            if number not in duplicates:
                duplicates.append(number)
                #print(duplicates)


def vertical_check():
    # Loops through all lists in matrix and then all numbers with
    # index "i" in those lists, appending them to duplicates to create columns.
    # The while loop causes the for loop to start the process over from the top
    # when the for loop finishes proccessing the current column.
    # index "i" is incremented by 1 to process the next column
    # when the length of duplicates reaches 8
    # - in preparation for the next loop.
    # duplicates is flushed when length reaches 9
    # and False returned if repeat numbers found in duplicates.
    
    duplicates = []
    i = 0
    count = 0

    while count < 9:
        count += 1
        for list_x in matrix:
            for number in list_x[i]:

                if len(duplicates) == 8:
                    i += 1
                
                if len(duplicates) == 9:
                    duplicates = []

                if number in duplicates:
                    #print("NOT SUDOKU (column)")
                    #print(list_x)
                    #print()
                    return False
                    
                if number not in duplicates:
                    duplicates.append(number)
                    #print(duplicates)


def sub_matrix(row, column):
    duplicates = []

    for i in range(3):
        for j in range(3):
            
            row_list = matrix[row+i]
            number = row_list[column+j]

            if number in duplicates:
                print("NOT SUDOKU (subgrid)")
                return False
                        
            if number not in duplicates:
                duplicates.append(number)
                print(duplicates)


def sub_matrix_check():
    for i in range(3):
        for j in range(3):
            print("I = " + str(i), "J = " + str(j*3))
            sub_matrix(i*3, j*3)


##matrix_temp = [['1','2','3','4','5','6','7','8','9'], \
##               ['4','5','6','7','8','9','1','2','3'], \
##               ['7','8','9','1','2','3','4','5','6'], \
##               ['1','2','3','4','5','6','7','8','9'], \
##               ['4','5','6','7','8','9','1','2','3'], \
##               ['7','8','9','1','2','3','4','5','6'], \
##               ['1','2','3','4','5','6','7','8','9'], \
##               ['4','5','6','7','8','9','1','2','3'], \
##               ['7','8','9','1','2','3','4','5','6']]
#matrix = matrix_temp

matrix = matrix_maker()
#print(matrix)
if horizontal_check() == False or vertical_check() == False or sub_matrix_check() == False:
    print("NOT SUDOKU")
else:
    print("SUDOKU!")


        

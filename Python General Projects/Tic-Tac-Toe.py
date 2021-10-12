from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    

    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.

    pos = validate_user_input()    
        
    available = make_list_of_free_fields(board)
    #print(available)      
    
    
    if pos == 1 and (0, 0) in available:
        board[0][0] = "O"
    elif pos == 2 and (0, 1) in available:
        board[0][1] = "O"
    elif pos == 3 and (0, 2) in available:
        board[0][2] = "O"
    elif pos == 4 and (1, 0) in available:
        board[1][0] = "O"
    elif pos == 6 and (1, 2) in available:
        board[1][2] = "O"
    elif pos == 7 and (2, 0) in available:
        board[2][0] = "O"
    elif pos == 8 and (2, 1) in available:
        board[2][1] = "O"
    elif pos == 9 and (2, 2) in available:
        board[2][2] = "O"
    else:
         print("\n\nPosition taken, choose another.")
         enter_move(board)

         
def validate_user_input():
    #This validates the user's input, restricting it to only integers
    #between 1-9 and asking for input again if invalid.
    
    X = True

    while X:
        try:
            pos = int(input("Enter Position: "))
            if pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                X = True
                print("Invalid Input. Choose a number from 1-9.\n\n")
            else:
                X = False
        except:
            X = True
            print("Invalid Input. Choose a number from 1-9.\n\n")

    return pos

            
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = ()

    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X", "O"]:
                item = (row, column)
                free_fields += (item, )
    
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False


def tie():
    # This function returns True if
    # there are no free fields left and no one has won.

    free = make_list_of_free_fields(board)
    
    if len(free) == 0 \
       and victory_for(board, "X") == False \
       and victory_for(board, "O") == False:
        print("DRAW")
        return True
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_fields = make_list_of_free_fields(board)

    cpu_move = randrange(len(free_fields))

    return free_fields[cpu_move]


def convert_to_pos(coordinate):
    # Converts tuple into position on board.

    if coordinate == (0, 0):
        board[0][0] = "X"
    elif coordinate == (0, 1):
        board[0][1] = "X"
    elif coordinate == (0, 2):
        board[0][2] = "X"
    elif coordinate == (1, 0):
        board[1][0] = "X"
    elif coordinate == (1, 2):
        board[1][2] = "X"
    elif coordinate == (2, 0):
        board[2][0] = "X"
    elif coordinate == (2, 1):
        board[2][1] = "X"
    elif coordinate == (2, 2):
        board[2][2] = "X"


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

display_board(board)

while True:
    enter_move(board)

    if tie() == True:
        break
    
    if victory_for(board, "O") == True:
        display_board(board)
        print("O Wins")
        break
    
    cpu_move = draw_move(board)
    convert_to_pos(cpu_move)

    display_board(board)

    if tie() == True:
        break

    if victory_for(board, "X") == True:
        display_board(board)
        print("X Wins")
        break


# Algorithm to verify the current (solution) state of the 9*9 sudoku board
# - takes as input: a 9*9 nested list of integers representing a sudoku board
# - If input sudoku board is consider solved:
#   - return True & print "SOLVED"
# - If not:
#   - return False & print "UNSOLVED, please continue playing!"
def verify_solution(sudoku_arr):

    # verify all cells contain value in range [1,9]
    for row in range(9):
        for col in range(9):
            # if current cell contains value out of range
            if sudoku_arr[row][col] > 9 or sudoku_arr[row][col] < 1:
                # display message to terminal
                print("NOT SOLVED, please continue playing!")
                return False

    # verify all rows contain cells with unique values
    for row in range(9):
        # array to store existence of a value in the current row
        value_existence = [0 for x in range(10)]
        for cell in range(9):
            # if value of current cell already exists in the current row
            if value_existence[sudoku_arr[row][cell]] == 1:
                # display message to terminal
                print("NOT SOLVED, please continue playing!")
                return False
            # if not, indicate its existence in the array
            else:
                value_existence[sudoku_arr[row][cell]] = 1

    # verify all columns contain cells with unique values
    for col in range(9):
        # array to store existence of a value in the current column
        value_existence = [0 for x in range(10)]
        for cell in range(9):
            # if value of current cell already exists in the current column
            if value_existence[sudoku_arr[cell][col]] == 1:
                # display message to terminal
                print("NOT SOLVED, please continue playing!")
                return False
            # if not, indicate its existence in the array
            else:
                value_existence[sudoku_arr[cell][col]] = 1
    
    # verify all blocks contain cells with unique values
    for row in range(0,9,3):
        for col in range(0,9,3):
            # array to store existence of a value in the current block
            value_existence = [0 for x in range(10)]
            # verify all cells in the current block contain unique values
            for subrow in range(row, row + 3):
                for subcol in range(col, col + 3):
                    # if value of current cell already exists in the current block
                    if value_existence[sudoku_arr[subrow][subcol]] == 1:
                        # display message to terminal
                        print("NOT SOLVED, please continue playing!")
                        return False
                    # if not, indicate its existence in the array
                    else:
                        value_existence[sudoku_arr[subrow][subcol]] = 1

    # if no rules are violated, display message to terminal
    print("SOLVED!")
    print()
    return True                 


# display the sudoku board in the terminal
# initial values are surrounded by "[]"
def print_sudoku_board(sudoku_arr, prefilled_cells):

    # iterate through all rows
    for row in range(9):
        # iterate through all columns
        for col in range(9):
            if prefilled_cells[row][col] == 1:
                print("[", end="")
            else:
                print(" ", end="")
            # print current cell to the terminal
            print(sudoku_arr[row][col], end="")
            # if current cell contains an initial value, surround it with "[]"
            if prefilled_cells[row][col] == 1:
                print("]", end=" ")
            else:
                print(" ", end=" ")
            
            # separate into blocks of 3 x 3 cells
            if col % 3 == 2:
                print("", end=" ")
        print()

        # separate into blocks of 3 x 3 cells
        if row % 3 == 2:
            print()


# prompt player for the row & column of the desired cell & a desired value
def get_players_move():
    
    user_input = [0,0,0]
    print("Please enter ROW of cell you wish to change (top=1, bottom=9):")
    # prompt player for input row
    input_row = input()
    user_input[0] = int(input_row) - 1
    print("Please enter COLUMN of cell you wish to change (left=1, right=9):")
    # prompt player for input column
    input_col = input()
    user_input[1] = int(input_col) - 1
    print("Please enter VALUE for chosen cell (1 to 9):")
    # prompt player for input value
    input_value = input()
    user_input[2] = int(input_value)

    return user_input


# determine if row, column, value entered by player is legal
def move_legal(move_arr, prefilled_cells):

    # check if row exists
    if move_arr[0] < 0 or move_arr[0] > 8:
        return False
    # check if column exists
    if move_arr[1] < 0 or move_arr[1] > 8:
        return False
    # check if value is in given range of n^2 values
    if move_arr[2] < 1 or move_arr[2] > 9:
        return False
    # check if cell contains an unchangeable/initialized value
    if prefilled_cells[move_arr[0]][move_arr[1]] == 1:
        return False
    return True

# - takes as input: a 9*9 sudoku nested list populated with 0 representing empty cells, and 1-9 representing pre-filled cells
# - while the sudoku puzzle isn't considered solved by the certification function:
#   - display "NOT SOLVED, please continue playing!"
#   - prompt player for input row, column, value
#   - display the updated board once player has entered a legal move
# - once the puzzle is considered solved by the certification function:
#   - display "SOLVED!"
#   - display the solved board
#   - terminate the program
def play_sudoku(sudoku_arr):

    # initialize array to indicate cells that have been been provided an unchangeable starting value
    prefilled_cells = [[0 for x in range(9)] for y in range(9)]
    # iterate each cell
    for row in range(9):
        for col in range(9):
            # if current cell has a non-zero value, indicate it in the array
            if sudoku_arr[row][col] != 0:
                prefilled_cells[row][col] = 1
  
    # while the sudoku puzzle is not verified to be solved by the verification algorithm
    while verify_solution(sudoku_arr) == False:
        print()
        # display current state of sudoku board
        print_sudoku_board(sudoku_arr, prefilled_cells)
        # prompt user for a legal move
        user_input_move = get_players_move()
        # while entered move isn't legal
        while move_legal(user_input_move, prefilled_cells) == False:
            print("Error: At least one of input cell & value is invalid!")
            # keep prompting user for a legal move
            user_input_move = get_players_move()
        # update sudoku board once a legal move has been entered by user
        sudoku_arr[user_input_move[0]][user_input_move[1]] = user_input_move[2]
    
    # once the sudoku puzzle has been solved, display "Solved!" message & display solved sudoku board
    print_sudoku_board(sudoku_arr, prefilled_cells)


# unsolved 9*9 sudoku puzzle with some cells that are initialized with values 
input_sudoku_board = [ [0,3,0,6,7,0,0,1,2], [6,0,2,1,9,5,3,4,8], [0,9,8,0,0,2,0,6,0],
                        [8,0,9,0,6,0,4,0,3], [4,0,6,8,0,3,7,0,1], [7,0,3,9,2,0,0,5,0],
                        [0,6,1,5,3,0,2,8,0], [2,8,0,4,0,9,0,0,5], [3,0,5,0,8,0,1,7,9] ]

# start the game with the provided unsolved 9*9 sudoku puzzle
play_sudoku(input_sudoku_board)

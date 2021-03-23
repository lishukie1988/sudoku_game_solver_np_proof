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


# return 1 if input value exists in the input row of the input sudoku nested array
# return 0 otherwise
def value_exists_in_row(value, sudoku_arr, row):

    # iterate every cell in the row
    for cell in range(9):
        # if current cell contains input value
        if sudoku_arr[row][cell] == value:
            return 1

    # return 0 if no cell contains the input value in the input row
    return 0


# return 1 if input value exists in the input column of the input sudoku nested array
# return 0 otherwise
def value_exists_in_col(value, sudoku_arr, col):

    # iterate every cell in the column
    for cell in range(9):
        # if current cell contains input value
        if sudoku_arr[cell][col] == value:
            return 1

    # return 0 if no cell contains the input value in the input column
    return 0


# return 1 if input value exists in the same block
# return 0 otherwise
def value_exists_in_block(value, sudoku_arr, row, col):

    # row of the top left cell of the block containing the input cell
    upper_left_row = (row // 3) * 3
    # column of the top left cell of the block containing the input cell
    upper_left_col = (col // 3) * 3

    # iterate every row in the block containing the value
    for row in range(upper_left_row, upper_left_row + 3):
        # iterate every column in the block containing the value
        for col in range(upper_left_col, upper_left_col + 3):
            # if current cell contains the input value
            if sudoku_arr[row][col] == value:
                return 1
    # return 0 if no cell in the block contains the input value 
    return 0


# return 1 if:
# - input value not in input row
# - input value not in input column
# - input value not in block containing input row & input column
# return 0 otherwise
def value_possible(value, sudoku_arr, row, col):

    # if input value not in input row
    if value_exists_in_row(value, sudoku_arr, row) == 1:
        return 0
    # if input value not in input column
    if value_exists_in_col(value, sudoku_arr, col) == 1:
        return 0
    # if input value not in block containing input row & input column
    if value_exists_in_block(value, sudoku_arr, row, col) == 1:
        return 0

    # return 1 otherwise
    return 1


# get the first empty cell encountered starting from row 0 & column 0
# - return 1 if such a cell exists
# - return 0 otherwise
def get_next_empty_cell(sudoku_arr, current_row, current_col):

    # iterate every row
    for row in range(9):
        # iterate every column
        for col in range(9):
            # if current cell empty
            if sudoku_arr[row][col] == 0:
                # fetch row of cell
                current_row[0] = row
                # fetch column of cell
                current_col[0] = col
                return 1

    # return 0 if no empty cell encountered
    return 0


# takes an unsolved sudoku board as input
# displays unsolved sudoku board
# solves sudoku board
# displays solved sudoku board
def find_sudoku_solution(sudoku_arr):

    # create nested array indicating cells with initial values (non-empty)
    prefilled_cells = [[0 for x in range(9)] for y in range(9)]
    # iterate every row
    for row in range(9):
        # iterate every column
        for col in range(9):
            # if current cell contains a value
            if sudoku_arr[row][col] != 0:
                # mark it as prefilled
                prefilled_cells[row][col] = 1

    print("Here is the input sudoku board:")
    # display unsolved sudoku board
    print_sudoku_board(sudoku_arr, prefilled_cells)

    # solve sudoku board
    sudoku_solver(sudoku_arr)

    # display solved sudoku board
    print("Here is the solved sudoku board:")
    print_sudoku_board(sudoku_arr, prefilled_cells)
        

# takes as input: a 9*9 sudoku nested list populated with 0 representing empty cells, and 1-9 representing pre-filled cells
# use a backtracking recursive algorithm to solve for the values of the empty cells (initially containing 0)
# mutates the nested array with solution values
def sudoku_solver(sudoku_arr):

    # row of current empty cell to be solved
    current_row = [0]
    # column of current empty cell to be solved
    current_col = [0]

    # attempt to get next empty/unsolved cell
    if get_next_empty_cell(sudoku_arr, current_row, current_col) == 0:
        # if no such cell exists, sudoku is solved
        return 1

    # iterate every allowed value
    for value in range(1,10):
        # if current value doesn't violate any sudoku rules
        if value_possible(value, sudoku_arr, current_row[0], current_col[0]):
            # assign value to current empty cell
            sudoku_arr[current_row[0]][current_col[0]] = value
            # if the remainder of the sudoku board can be recursively solved with this algorithm based on this value assignment
            if sudoku_solver(sudoku_arr) == 1:
                # sudoku is solved, all values assigned in the process are stored in the sudoku nested array
                return 1
            # otherwise, revert the value of the current cell back to 0 (empty)
            else:
                sudoku_arr[current_row[0]][current_col[0]] = 0

    # return 0 to indicate that no solution exists for current state of sudoku board
    return 0


# unsolved 9*9 input sudoku board
input_sudoku_board = [ [5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0],
                        [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6],
                        [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9] ]

# find solution to the unsolved input sudoku board
find_sudoku_solution(input_sudoku_board)
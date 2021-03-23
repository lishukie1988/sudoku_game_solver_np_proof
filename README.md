#sudoku

- For sudoku_game.py:

  - please run sudoku_game.py using the following command: python3 sudoku_game.py
  - a default 9 * 9 input puzzle is used for the program, but it is possible for the program to take in any 9 * 9 nested list containing integers from 1 to 9
  - upon execution, the program will:
    - display the start state of the puzzle in the console
    - prompt the user for the first move
  - after each move entered by the user, the verification algorithm is executed and either of the following messages will be displayed in the console:
    - "SOLVED!" // the program will then terminate
    - "NOT SOLVED, please continue playing!" // the new state of the puzzle will be displayed
					   // the user will be prompted for the next move


- For sudoku_solver.py:

  - please run sudoku_solver.py using the following command: python3 sudoku_solver.py
  - a default 9 * 9 input puzzle is used for the program, but it is possible for the program to take in any 9 * 9 nested list containing integers from 1 to 9
  - upon execution, the program will display in the console:
    - the start state of the puzzle
    - the solved state of the puzzle


- For both files:

  - please expand the console window for better experience
  - below is the solution for the default input sudoku puzzle:

     [5] [3]  4    6  [7]  8    9   1   2   
     [6]  7   2   [1] [9] [5]   3   4   8   
      1  [9] [8]   3   4   2    5  [6]  7   

     [8]  5   9    7  [6]  1    4   2  [3]  
     [4]  2   6   [8]  5  [3]   7   9  [1]  
     [7]  1   3    9  [2]  4    8   5  [6]  

      9  [6]  1    5   3   7   [2] [8]  4   
      2   8   7   [4] [1] [9]   6   3  [5]  
      3   4   5    2  [8]  6    1  [7] [9]  



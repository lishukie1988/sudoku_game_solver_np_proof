#sudoku

- Summary:
  - This repository contains 3 files:
    - sudoku_game.py: allows the user to solve a given 9 * 9 Sudoku puzzle
    - sudoku_solver.py: solves a given 9 * 9 Sudoku puzzle
    - proof.txt: proof that Sudoku is an intractable decision problem in NP with a non-polynomial time complexity

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

     row 1: [5] [3]  4   6  [7]  8   9   1   2   
     row 2: [6]  7   2  [1] [9] [5]  3   4   8   
     row 3:  1  [9] [8]  3   4   2   5  [6]  7   
     row 4: [8]  5   9   7  [6]  1   4   2  [3]  
     row 5: [4]  2   6  [8]  5  [3]  7   9  [1]  
     row 6: [7]  1   3   9  [2]  4   8   5  [6]  
     row 7:  9  [6]  1   5   3   7  [2] [8]  4   
     row 8:  2   8   7  [4] [1] [9]  6   3  [5]  
     row 9:  3   4   5   2  [8]  6   1  [7] [9]  



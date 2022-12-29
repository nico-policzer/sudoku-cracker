# sudoku-cracker

**A python script which solves a sudoku puzzle using optimized brute force methods**

Sudoku Rules can be found here: https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/

Sudoku puzzles are represented as 81 long lists of numbers 0-9, 0 represents a blank space.

**Example of an unsolved board:** 

                  [5, 0, 0, 0, 0, 0, 0, 0, 9,
                   0, 0, 9, 3, 0, 0, 0, 0, 0,
                   0, 2, 7, 0, 0, 0, 1, 0, 0,
                   4, 0, 0, 5, 0, 0, 3, 0, 8,
                   0, 1, 0, 0, 0, 6, 0, 5, 7,
                   0, 0, 3, 0, 0, 0, 9, 0, 0,
                   9, 0, 0, 0, 4, 5, 0, 0, 3,
                   1, 0, 0, 0, 7, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 6, 0, 5]
                   
**Example solved Board:** 
                  
                 [5, 3, 1, 7, 6, 2, 8, 4, 9,
                  6, 4, 9, 3, 8, 1, 5, 7, 2,
                  8, 2, 7, 4, 5, 9, 1, 3, 6,
                  4, 9, 6, 5, 1, 7, 3, 2, 8,
                  2, 1, 8, 9, 3, 6, 4, 5, 7,
                  7, 5, 3, 8, 2, 4, 9, 6, 1,
                  9, 6, 2, 1, 4, 5, 7, 8, 3,
                  1, 8, 5, 6, 7, 3, 2, 9, 4,
                  3, 7, 4, 2, 9, 8, 6, 1, 5]
                 
To solve a sudoku puzzle that is represented as specified above, call solve(board) with sudoku board. The method will return true if it reaches a solution(the board is solvable) and false if there are no possible solutions from boards intial state.

To see the solved board, you can simply print the board after calling solve using print(board) or print_board(board)

This program will start from the first blank space(represented by 0), and do a backtracking search by trying numbers 1-9, using only those which do not break sudokus rules. If no valid moves are available, the solve method will return false and backtrack.

Once the board has no empty spaces, since only valid moves were played, the solve method will return true indicating the board has been solved.


In  src/test_sudoku_cracker.py I have included a commented out test in test_solve which tests my sudoku solver on the so called hardest sudoku ever made, written by mathematician Arto Inkala.

Source: https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku

I have commented out this test because it takes my program around 17 seconds to solve, feel free to uncomment it.


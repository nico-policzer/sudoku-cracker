

def solve(puzzle: list) -> bool:
    # FIXME: maybe I return puzzle after completion? Otherwise return false?
    # solves sudoku board "puzzle", return True when solved, returns false if unsolvable
    # solves by updating puzzle list to reflect different sudoku states
    # REQUIRES: "puzzle" is an 81 long item list representing a 9x9 sudoku board, containing only digits 0-9
    # a 0 represents a blank(unfilled) spot, other digits represent filled spots.
    # the state of the sudoku board "puzzle" represents must be a valid sudoku board, meaning no duplicate digits in
    # rows, columns or the 9 3x3 blocks.

    if puzzle.count(0) == 0:
        # since puzzle is a valid sudoku board which follows all sudoku's rules, if there are no blanks, it is solved
        return True

    first_blank = puzzle.index(0)
    for i in range(1, 10):
        if valid(i, first_blank, puzzle):
            puzzle[first_blank] = i
            solved_puzzle = solve(puzzle)
            if solved_puzzle:
                return True
            puzzle[first_blank] = 0 # if board cannot be solved using i in first_blank, resets first_blank to blank

    return False # no valid moves it can play from this state, returns false


def valid(i: int, first_blank: int, puzzle: list) -> bool:
    # REQUIRES: 1 <= i <= 9, 0<= first_blank <= 81, puzzle represents sudoku board
    # returns true if i can be validly played in position first_blank on puzzle
    # must follow sudoku rules - no duplicates in row, column or 3x3 block it is a member of.
    # otherwise returns false
    rows = to_rows(puzzle)
    row = rows[first_blank // 9]
    columns = to_columns(puzzle)
    column = columns[first_blank % 9]
    blocks = to_blocks(puzzle)
    block = blocks[get_block_index(first_blank)]
    return row.count(i) == 0 and column.count(i) == 0 and block.count(i) == 0


def to_rows(puzzle: list) -> list:
    # returns list of all rows in 9x9 puzzle from top to bottom
    # each row is a list of contents from left to right on board

    rows = []
    for row_index in range(9):
        row = []
        for i in range(9):
            row.append(puzzle[i + (row_index * 9)])
        rows.append(row)
    return rows


def to_columns(puzzle: list) -> list:
    # returns list of all columns in 9x9 puzzle from left to right
    # each column is a list of contents from top to bottom on board

    columns = []
    for column_index in range(9):
        column = []
        for i in range(9):
            column.append(puzzle[column_index + (i * 9)])
        columns.append(column)
    return columns


def to_blocks(puzzle: list) -> list:
    # returns list of all 9 3x3 blocks in 9x9 puzzle, from top left to bottom right
    # each 3x3 block is a list of contents from top left to bottom right

    blocks = []
    for block_row in range(3):
        for block_column in range(3):
            start = (3 * block_column) + (27 * block_row)
            block = get_block(puzzle, start)
            blocks.append(block)
    return blocks


def get_block(puzzle: list, start: int) -> list:
    # returns list of contents of 3x3 block in puzzle with top left corner at start
    # contents are returned in order from top left to bottom right of 3x3 block
    # requires: int is one of {0, 3, 6, 27, 30, 33, 54, 57, 60}

    block = []
    for i in range(3):
        for x in range(3):
            block.append(puzzle[start + x + (i * 9)])
    return block


def get_block_index(i: int) -> int:
    # returns index of 3x3 block from a 9x9 puzzle which index i from list representing puzzle is a part of
    column = (i % 9) // 3
    row = i // 27
    return (row * 3) + column


def print_board(puzzle):
    # prints puzzle as a 9x9 sudoku board
    for row in to_rows(puzzle):
        print(row)
    print()


import unittest
from sudoku_cracker import *


class SudokuCrackerTest(unittest.TestCase):

    blank = [0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0]

    p1_solved = [7, 3, 5, 6, 1, 4, 8, 9, 2,
                 8, 4, 2, 9, 7, 3, 5, 6, 1,
                 9, 6, 1, 2, 8, 5, 3, 7, 4,
                 2, 8, 6, 3, 4, 9, 1, 5, 7,
                 4, 1, 3, 8, 5, 7, 9, 2, 6,
                 5, 7, 9, 1, 2, 6, 4, 3, 8,
                 1, 5, 7, 4, 9, 2, 6, 8, 3,
                 6, 9, 4, 7, 3, 8, 2, 1, 5,
                 3, 2, 8, 5, 6, 1, 7, 4, 9]

    p1_almost_solved = [7, 3, 5, 6, 1, 4, 8, 9, 2,
                        8, 4, 2, 9, 7, 3, 5, 6, 1,
                        9, 6, 1, 2, 8, 5, 3, 7, 4,
                        2, 8, 6, 3, 4, 9, 1, 5, 7,
                        4, 1, 3, 8, 5, 7, 9, 2, 6,
                        5, 7, 9, 1, 2, 6, 4, 3, 8,
                        1, 5, 7, 4, 9, 2, 6, 8, 3,
                        6, 9, 4, 7, 3, 8, 2, 1, 5,
                        3, 2, 8, 5, 6, 1, 7, 4, 0]

    p1_unsolved = [0, 3, 5, 6, 1, 4, 8, 9, 2,
                   8, 4, 2, 9, 7, 0, 5, 0, 0,
                   9, 0, 1, 2, 0, 0, 3, 0, 0,
                   2, 8, 6, 3, 4, 9, 1, 5, 7,
                   4, 1, 0, 0, 0, 7, 9, 2, 6,
                   5, 7, 9, 1, 2, 6, 4, 3, 8,
                   1, 0, 7, 4, 9, 2, 6, 8, 3,
                   6, 9, 4, 7, 3, 8, 2, 1, 5,
                   3, 2, 0, 5, 6, 1, 7, 4, 0]

    # from https://sudoku.com/hard/
    p2_unsolved = [5, 0, 0, 0, 0, 0, 0, 0, 9,
                   0, 0, 9, 3, 0, 0, 0, 0, 0,
                   0, 2, 7, 0, 0, 0, 1, 0, 0,
                   4, 0, 0, 5, 0, 0, 3, 0, 8,
                   0, 1, 0, 0, 0, 6, 0, 5, 7,
                   0, 0, 3, 0, 0, 0, 9, 0, 0,
                   9, 0, 0, 0, 4, 5, 0, 0, 3,
                   1, 0, 0, 0, 7, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 6, 0, 5]

    p2_solved = [5, 3, 1, 7, 6, 2, 8, 4, 9,
                 6, 4, 9, 3, 8, 1, 5, 7, 2,
                 8, 2, 7, 4, 5, 9, 1, 3, 6,
                 4, 9, 6, 5, 1, 7, 3, 2, 8,
                 2, 1, 8, 9, 3, 6, 4, 5, 7,
                 7, 5, 3, 8, 2, 4, 9, 6, 1,
                 9, 6, 2, 1, 4, 5, 7, 8, 3,
                 1, 8, 5, 6, 7, 3, 2, 9, 4,
                 3, 7, 4, 2, 9, 8, 6, 1, 5]

    p2_to_rows = [[5, 0, 0, 0, 0, 0, 0, 0, 9],
                  [0, 0, 9, 3, 0, 0, 0, 0, 0],
                  [0, 2, 7, 0, 0, 0, 1, 0, 0],
                  [4, 0, 0, 5, 0, 0, 3, 0, 8],
                  [0, 1, 0, 0, 0, 6, 0, 5, 7],
                  [0, 0, 3, 0, 0, 0, 9, 0, 0],
                  [9, 0, 0, 0, 4, 5, 0, 0, 3],
                  [1, 0, 0, 0, 7, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 6, 0, 5]]

    p2_to_columns = [[5, 0, 0, 4, 0, 0, 9, 1, 0],
                     [0, 0, 2, 0, 1, 0, 0, 0, 0],
                     [0, 9, 7, 0, 0, 3, 0, 0, 0],
                     [0, 3, 0, 5, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 4, 7, 0],
                     [0, 0, 0, 0, 6, 0, 5, 0, 0],
                     [0, 0, 1, 3, 0, 9, 0, 0, 6],
                     [0, 0, 0, 0, 5, 0, 0, 0, 0],
                     [9, 0, 0, 8, 7, 0, 3, 0, 5]]

    p2_to_blocks = [[5, 0, 0, 0, 0, 9, 0, 2, 7],
                    [0, 0, 0, 3, 0, 0, 0, 0, 0],
                    [0, 0, 9, 0, 0, 0, 1, 0, 0],
                    [4, 0, 0, 0, 1, 0, 0, 0, 3],
                    [5, 0, 0, 0, 0, 6, 0, 0, 0],
                    [3, 0, 8, 0, 5, 7, 9, 0, 0],
                    [9, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 4, 5, 0, 7, 0, 0, 0, 0],
                    [0, 0, 3, 0, 0, 0, 6, 0, 5]]

    p1_almost_solved_block_0 = [0, 3, 5, 8, 4, 2, 9, 0, 1]
    p1_almost_solved_block_3 = [6, 1, 4, 9, 7, 0, 2, 0, 0]
    p1_almost_solved_block_6 = [8, 9, 2, 5, 0, 0, 3, 0, 0]
    p1_almost_solved_block_27 = [2, 8, 6, 4, 1, 0, 5, 7, 9]
    p1_almost_solved_block_30 = [3, 4, 9, 0, 0, 7, 1, 2, 6]
    p1_almost_solved_block_33 = [1, 5, 7, 9, 2, 6, 4, 3, 8]
    p1_almost_solved_block_54 = [1, 0, 7, 6, 9, 4, 3, 2, 0]
    p1_almost_solved_block_57 = [4, 9, 2, 7, 3, 8, 5, 6, 1]
    p1_almost_solved_block_60 = [6, 8, 3, 2, 1, 5, 7, 4, 0]

    # So called "Hardest Sudoku ever made" - Arto Inkala
    # https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku
    arto_inkala_sudoku = [8, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 3, 6, 0, 0, 0, 0, 0,
                          0, 7, 0, 0, 9, 0, 2, 0, 0,
                          0, 5, 0, 0, 0, 7, 0, 0, 0,
                          0, 0, 0, 0, 4, 5, 7, 0, 0,
                          0, 0, 0, 1, 0, 0, 0, 3, 0,
                          0, 0, 1, 0, 0, 0, 0, 6, 8,
                          0, 0, 8, 5, 0, 0, 0, 1, 0,
                          0, 9, 0, 0, 0, 0, 4, 0, 0]

    inkala_solved = [8, 1, 2, 7, 5, 3, 6, 4, 9,
                     9, 4, 3, 6, 8, 2, 1, 7, 5,
                     6, 7, 5, 4, 9, 1, 2, 8, 3,
                     1, 5, 4, 2, 3, 7, 8, 9, 6,
                     3, 6, 9, 8, 4, 5, 7, 2, 1,
                     2, 8, 7, 1, 6, 9, 5, 3, 4,
                     5, 2, 1, 9, 7, 4, 3, 6, 8,
                     4, 3, 8, 5, 2, 6, 9, 1, 7,
                     7, 9, 6, 3, 1, 8, 4, 5, 2]

    def test_to_rows(self):
        self.assertEqual(to_rows(self.p2_unsolved), self.p2_to_rows)

    def test_to_columns(self):
        self.assertEqual(to_columns(self.p2_unsolved), self.p2_to_columns)

    def test_to_blocks(self):
        self.assertEqual(to_blocks(self.p2_unsolved), self.p2_to_blocks)

    def test_get_block(self):
        self.assertEqual(get_block(self.p1_unsolved, 0),
                         self.p1_almost_solved_block_0)
        self.assertEqual(get_block(self.p1_unsolved, 3),
                         self.p1_almost_solved_block_3)
        self.assertEqual(get_block(self.p1_unsolved, 6),
                         self.p1_almost_solved_block_6)
        self.assertEqual(get_block(self.p1_unsolved, 27),
                         self.p1_almost_solved_block_27)
        self.assertEqual(get_block(self.p1_unsolved, 30),
                         self.p1_almost_solved_block_30)
        self.assertEqual(get_block(self.p1_unsolved, 33),
                         self.p1_almost_solved_block_33)
        self.assertEqual(get_block(self.p1_unsolved, 54),
                         self.p1_almost_solved_block_54)
        self.assertEqual(get_block(self.p1_unsolved, 57),
                         self.p1_almost_solved_block_57)
        self.assertEqual(get_block(self.p1_unsolved, 60),
                         self.p1_almost_solved_block_60)

    def test_valid(self):
        self.assertTrue(valid(6, 1, self.arto_inkala_sudoku))
        self.assertFalse(valid(8, 9, self.arto_inkala_sudoku))
        self.assertTrue(valid(9, 80, self.p1_unsolved))
        self.assertFalse(valid(4, 17, self.p1_unsolved))
        self.assertFalse(valid(7, 1, self.p2_unsolved))
        self.assertFalse(valid(1, 1, self.p2_unsolved))
        self.assertFalse(valid(3, 9, self.p2_unsolved))

    def test_solve(self):
        # p_hard_copy = self.arto_inkala_sudoku.copy()
        # UNCOMMENT BELOW TO TEST ARTO INKALA HARD SUDOKU - WILL TAKE AROUND 17 seconds
        # p_hard_copy = self.arto_inkala_sudoku.copy()
        # solve(p_hard_copy)
        # self.assertEquals(p_hard_copy, self.arto_solved)

        p2_copy = self.p2_unsolved.copy()
        solve(p2_copy)
        self.assertEquals(p2_copy, self.p2_solved)

        p1_copy = self.p1_unsolved.copy()
        solve(p1_copy)
        self.assertEquals(p1_copy, self.p1_solved)

        p1_almost_solved_copy = self.p1_almost_solved.copy()
        solve(p1_almost_solved_copy)
        self.assertEquals(p1_almost_solved_copy, self.p1_solved)

    def test_get_block_index(self):
        self.assertEqual(get_block_index(0), 0)
        self.assertEqual(get_block_index(8), 2)
        self.assertEqual(get_block_index(11), 0)
        self.assertEqual(get_block_index(22), 1)
        self.assertEqual(get_block_index(0), 0)
        self.assertEqual(get_block_index(80), 8)
        self.assertEqual(get_block_index(27), 3)
        self.assertEqual(get_block_index(54), 6)
        self.assertEqual(get_block_index(58), 7)


if __name__ == '__main__':
    unittest.main()

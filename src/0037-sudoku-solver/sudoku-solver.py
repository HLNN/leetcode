# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# 	Each of the digits 1-9 must occur exactly once in each row.
# 	Each of the digits 1-9 must occur exactly once in each column.
# 	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# 	The given board contain only digits 1-9 and the character '.'.
# 	You may assume that the given Sudoku puzzle will have a single unique solution.
# 	The given board size is always 9x9.
#
#


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def nextPoint(i, j):
            j += 1
            if j == 9:
                j = 0
                i += 1
                if i == 9:
                    return -1, -1
            return i, j
        
        def bt(board, ht, p):
            if p == (-1, -1):
                return True
            i, j = p
            if board[i][j] != ".":
                if bt(board, ht, nextPoint(i, j)):
                    return True
            else:
                for n in range(9):
                    if ht[0][i][n] and ht[1][j][n] and ht[2][i // 3 * 3 + j // 3][n]:
                        ht[0][i][n] = False
                        ht[1][j][n] = False
                        ht[2][i // 3 * 3 + j // 3][n] = False
                        board[i][j] = str(n + 1)
                        if bt(board, ht, nextPoint(i, j)):
                            return True
                        ht[0][i][n] = True
                        ht[1][j][n] = True
                        ht[2][i // 3 * 3 + j // 3][n] = True
                        board[i][j] = "."
                        
            
        ht = [[[True for _ in range(9)] for _ in range(9)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ht[0][i][int(board[i][j]) - 1] = False
                    ht[1][j][int(board[i][j]) - 1] = False
                    ht[2][i // 3 * 3 + j // 3][int(board[i][j]) - 1] = False
        
        bt(board, ht, (0, 0))
        

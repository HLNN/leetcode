# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#
# 	Each row must contain the digits 1-9 without repetition.
# 	Each column must contain the digits 1-9 without repetition.
# 	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#
# Note:
#
#
# 	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# 	Only the filled cells need to be validated according to the mentioned rules.
#
#
#  
# Example 1:
#
#
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
#  
# Constraints:
#
#
# 	board.length == 9
# 	board[i].length == 9
# 	board[i][j] is a digit or '.'.
#
#


class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [[{}, {}, {}] for _ in range(3)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i] or num in cols[j] or num in boxes[math.floor(i / 3)][math.floor(j / 3)]:
                    return False
                rows[i][num] = True
                cols[j][num] = True
                boxes[math.floor(i / 3)][math.floor(j / 3)][num] = True 
        return True
    

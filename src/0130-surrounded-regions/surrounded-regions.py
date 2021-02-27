# Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#  
# Example 1:
#
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 200
# 	board[i][j] is 'X' or 'O'.
#
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 2 or len(board[0]) < 2: return
        def valid(i, j):
            return  i >=0 and j >= 0 and i < len(board) and j < len(board[0])
        
        def dfs(i, j, diff):
            board[i][j] = "Y"
            for n in range(4):
                ni = i + diff[n][0]
                nj = j + diff[n][1]
                if valid(ni, nj) and board[ni][nj] == "O":
                    dfs(ni, nj, diff)
            
        diff = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0, diff)
            if board[i][len(board[0]) - 1] == "O":
                dfs(i, len(board[0]) - 1, diff)
            
        for j in range(1, len(board[0])):
            if board[0][j] == "O":
                dfs(0, j, diff)
            if board[len(board) - 1][j] == "O":
                dfs(len(board) - 1, j, diff)
                
        for i, j in product(range(len(board)), range(len(board[0]))):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "Y":
                board[i][j] = "O"
                
        

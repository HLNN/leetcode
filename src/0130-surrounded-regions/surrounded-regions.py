# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#  
# Example 1:
#
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
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
        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'Z'
                nei = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for di, dj in nei:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < n and 0 <= jj < m:
                        dfs(ii, jj)
        
        n, m = len(board), len(board[0])
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)
        
        for i in range(n):
            for j in range(m):
                board[i][j] = 'O' if board[i][j] == 'Z' else 'X'
    

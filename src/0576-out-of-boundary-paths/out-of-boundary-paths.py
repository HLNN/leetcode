# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
#
# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
#
#
# Example 2:
#
#
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
#
#
#  
# Constraints:
#
#
# 	1 <= m, n <= 50
# 	0 <= maxMove <= 50
# 	0 <= startRow < m
# 	0 <= startColumn < n
#
#


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        m, n = m - 1, n - 1
        @cache
        def dp(x, y, i):
            if x < 0 or x > m or y < 0 or y > n or i < 1: return 0
            if i == 1: return sum((x == 0, x == m, y == 0, y == n))
            if x >= i and m - x >= i and y >= i and n - y >= i: return 0
            
            return sum(dp(x + dx, y + dy, i - 1) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        
        return sum(dp(startRow, startColumn, i) for i in range(1, maxMove + 1)) % 1000000007
    

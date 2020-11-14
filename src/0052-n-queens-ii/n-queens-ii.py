# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#  
# Example 1:
#
#
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 9
#
#


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, xyDiff, xySum):
            p = len(queens)
            if p == n:
                self.res += 1
                return
            for q in range(n):
                if q not in queens and p-q not in xyDiff and p+q not in xySum:
                    dfs(queens+[q], xyDiff+[p-q], xySum+[p+q])
        
        self.res = 0
        dfs([], [], [])
        return self.res

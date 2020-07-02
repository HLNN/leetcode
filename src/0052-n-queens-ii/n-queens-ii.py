# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
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

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
#


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xyDiff, xySum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xyDiff and p+q not in xySum:
                    dfs(queens+[q], xyDiff+[p-q], xySum+[p+q])
        
        res = []
        dfs([], [], [])
        return [["." * i + "Q" + "." * (n-i-1) for i in queens] for queens in res]
                

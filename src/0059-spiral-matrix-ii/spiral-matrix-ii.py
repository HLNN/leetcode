# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
#
#


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = d = i = 0
        for _ in range(n * n):
            i += 1
            m[r][c] = i
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and m[nr][nc] == 0:
                r, c = nr, nc
            else:
                d = (d + 1) % 4
                r, c = r + dr[d], c + dc[d]
        return m
    

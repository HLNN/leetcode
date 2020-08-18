# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
#
# Follow up:
#
#
# 	A straight forward solution using O(mn) space is probably a bad idea.
# 	A simple improvement uses O(m + n) space, but still not the best solution.
# 	Could you devise a constant space solution?
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[0].length
# 	1 <= m, n <= 200
# 	-10^9 <= matrix[i][j] <= 10^9
#
#


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return matrix
        n, m = len(matrix), len(matrix[0])
        r, c = False, False
        for i in range(n):
            if matrix[i][0] == 0:
                r = True
        for j in range(m):
            if matrix[0][j] == 0:
                c = True
        
        for i, j in product(range(1, n), range(1, m)):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
        
        if r:
            for i in range(n):
                matrix[i][0] = 0
        if c:
            for j in range(m):
                matrix[0][j] = 0
        

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 100
# 	-104 <= matrix[i][j], target <= 104
#
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        while l <= r:
            x = (l + r) // 2
            if matrix[x][0] <= target and (x + 1 >= n or target < matrix[x+1][0]):
                break
            elif target < matrix[x][0]:
                r = x - 1
            else:
                l = x + 1
        
        l, r = 0, m - 1
        while l <= r:
            y = (l + r) // 2
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = y + 1
            else:
                r = y - 1
        return False
    

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and space is marked as 1 and 0 respectively in the grid.
#
#  
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	m == obstacleGrid.length
# 	n == obstacleGrid[i].length
# 	1 <= m, n <= 100
# 	obstacleGrid[i][j] is 0 or 1.
#
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        if obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = 1
        
        for i in range(1, m):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1 else 0
        for j in range(1, n):
            obstacleGrid[0][j] = 1 if obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1 else 0
        
        for i, j in product(range(1, m), range(1, n)):
            obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

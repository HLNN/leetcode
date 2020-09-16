# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#  
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
#
#
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
#
#
# Input: grid = [[1,0]]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	row == grid.length
# 	col == grid[i].length
# 	1 <= row, col <= 100
# 	grid[i][j] is 0 or 1.
#
#


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not len(grid[0]): return 0
        res = 0
        if grid[0][0]: res += 4
        
        for i in range(1, len(grid[0])):
            if grid[0][i]:
                if grid[0][i-1]:
                    res += 2
                else:
                    res += 4
        for i in range(1, len(grid)):
            if grid[i][0]:
                if grid[i-1][0]:
                    res += 2
                else:
                    res += 4
        for i, j in product(range(1, len(grid)), range(1, len(grid[0]))):
            if grid[i][j]:
                res += 4 - 2 * (grid[i][j-1] + grid[i-1][j])
        
        return res
    

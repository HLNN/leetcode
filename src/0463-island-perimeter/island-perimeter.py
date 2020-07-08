# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#  
#
# Example:
#
#
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
#
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
    

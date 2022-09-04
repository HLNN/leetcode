# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#  
# Example 1:
#
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 300
# 	grid[i][j] is '0' or '1'.
#
#


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n:
                if (i, j) in seen or grid[i][j] == '0': return
                
                seen.add((i, j))
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(i + di, j + dj)
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == '1' and (i, j) not in seen:
                res += 1
                dfs(i, j)
        
        return res
    

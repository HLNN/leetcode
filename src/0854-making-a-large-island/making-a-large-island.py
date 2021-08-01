# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
#
# Return the size of the largest island in grid after applying this operation.
#
# An island is a 4-directionally connected group of 1s.
#
#  
# Example 1:
#
#
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
#
# Example 2:
#
#
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
#
# Example 3:
#
#
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#
#  
# Constraints:
#
#
# 	n == grid.length
# 	n == grid[i].length
# 	1 <= n <= 500
# 	grid[i][j] is either 0 or 1.
#


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, index):
            ans = 1
            grid[i][j] = index
            for di, dj in [(1, 0), [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i+di < n and 0 <= j+dj < n and grid[i+di][j+dj] == 1:
                    ans += dfs(i+di, j+dj, index)
            return ans
            
        n, index, island = len(grid), 2, {}
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 1:
                island[index] = dfs(i, j, index)
                index += 1
            
        ans = max(island.values() or [0])
        for i, j in product(range(n), range(n)):
            if grid[i][j] == 0:
                neighbor = {grid[i+di][j+dj] for di, dj in [(1, 0), [-1, 0], [0, 1], [0, -1]] if 0 <= i+di < n and 0 <= j+dj < n and grid[i+di][j+dj] > 1}
                ans = max(ans, 1 + sum(island[index] for index in neighbor))
        
        return ans
    

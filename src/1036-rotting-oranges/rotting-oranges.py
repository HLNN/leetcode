# You are given an m x n grid where each cell can have one of three values:
#
#
# 	0 representing an empty cell,
# 	1 representing a fresh orange, or
# 	2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#  
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 10
# 	grid[i][j] is 0, 1, or 2.
#
#


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i, j))
            if grid[i][j] == 1: fresh += 1
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            levels = 0
            
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
        
        return -1 if fresh != 0 else max(levels-1, 0)
    

# You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.
#
# Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.
#
# Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
#
#  
# Example 1:
#
#
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#  
# Constraints:
#
#
# 	m == heights.length
# 	n == heights[i].length
# 	1 <= m, n <= 200
# 	1 <= heights[i][j] <= 105
#
#


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        
        n, m = len(matrix), len(matrix[0])
        
        pacific = deque()
        atlantic = deque()
        
        for i in range(n):
            pacific.append((i, 0))
            atlantic.append((i, m - 1))
        for j in range(m):
            pacific.append((0, j))
            atlantic.append((n - 1, j))
        
        def bfs(queue):
            reachable = set()
            while queue:
                r, c = queue.popleft()
                reachable.add((r, c))
                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + x, c + y
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in reachable:
                        if matrix[nr][nc] >= matrix[r][c]: queue.append((nr, nc))
            return reachable
        
        pacific = bfs(pacific)
        atlantic = bfs(atlantic)
        
        return list(pacific.intersection(atlantic))
    

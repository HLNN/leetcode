# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
#
#
# 	The order of returned grid coordinates does not matter.
# 	Both m and n are less than 150.
#
#
#  
#
# Example:
#
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
#
#
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
    

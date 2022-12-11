# You are given an m x n integer matrix grid and an array queries of size k.
#
# Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:
#
#
# 	If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# 	Otherwise, you do not get any points, and you end this process.
#
#
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
#
# Return the resulting array answer.
#
#  
# Example 1:
#
#
# Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
# Output: [5,8,1]
# Explanation: The diagrams above show which cells we visit to get points for each query.
#
# Example 2:
#
#
# Input: grid = [[5,2,1],[1,1,2]], queries = [3]
# Output: [0]
# Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	2 <= m, n <= 1000
# 	4 <= m * n <= 105
# 	k == queries.length
# 	1 <= k <= 104
# 	1 <= grid[i][j], queries[i] <= 106
#
#


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        seen = set()
        heap = [(grid[0][0] + 1, 0, 0)]
        
        while heap:
            v, x, y = heappop(heap)
            if (x, y) not in seen:
                seen.add((x, y))
                grid[x][y] = v
                
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                        heappush(heap, (max(v, grid[nx][ny] + 1), nx, ny))
        
        cnt = Counter(chain(*grid))
        cnt = sorted(list(cnt.items()))
        idxs, cnt = zip(*cnt)
        # print(idxs, cnt)
        cnt = list(accumulate(cnt))
        # print(cnt)
        
        res = []
        for q in queries:
            if q >= idxs[-1]:
                res.append(cnt[-1])
            elif q < idxs[0]:
                res.append(0)
            else:
                idx = bisect.bisect(idxs, q)
                if q < idxs[idx]: idx -= 1
                res.append(cnt[idx])
        return res
    

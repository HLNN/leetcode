# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
#
# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
#
#
# 	The rank is an integer starting from 1.
# 	If two elements p and q are in the same row or column, then:
#
# 		If p < q then rank(p) < rank(q)
# 		If p == q then rank(p) == rank(q)
# 		If p > q then rank(p) > rank(q)
#
#
# 	The rank should be as small as possible.
#
#
# It is guaranteed that answer is unique under the given rules.
#
#  
# Example 1:
#
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
#
#
# Example 2:
#
#
# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
#
#
# Example 3:
#
#
# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
#
#
# Example 4:
#
#
# Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
# Output: [[5,1,4],[1,2,3],[6,3,1]]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 500
# 	-109 <= matrix[row][col] <= 109
#
#


class DSU:
    def __init__(self, graph):
        self.p = {i:i for i in graph}
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
    
    def groups(self):
        ans = defaultdict(list)
        for el in self.p.keys():
            ans[self.find(el)].append(el)
        return ans

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = defaultdict(list)
        
        for i, j in product(range(m), range(n)):
            d[matrix[i][j]].append([i, j])
        
        for a in sorted(d):
            graph = [i for i, j in d[a]] + [j + m for i, j in d[a]]
            dsu = DSU(graph)
            for i, j in d[a]: dsu.union(i, j + m)
            
            for group in dsu.groups().values():
                mx = max(rank[i] for i in group)
                for i in group: rank[i] = mx + 1
            
            for i, j in d[a]: matrix[i][j] = rank[i]
        
        return matrix
    

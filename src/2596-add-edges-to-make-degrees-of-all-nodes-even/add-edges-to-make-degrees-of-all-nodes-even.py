# There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.
#
# You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.
#
# Return true if it is possible to make the degree of each node in the graph even, otherwise return false.
#
# The degree of a node is the number of edges connected to it.
#
#  
# Example 1:
#
#
# Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
# Output: true
# Explanation: The above diagram shows a valid way of adding an edge.
# Every node in the resulting graph is connected to an even number of edges.
#
#
# Example 2:
#
#
# Input: n = 4, edges = [[1,2],[3,4]]
# Output: true
# Explanation: The above diagram shows a valid way of adding two edges.
#
# Example 3:
#
#
# Input: n = 4, edges = [[1,2],[1,3],[1,4]]
# Output: false
# Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
#
#  
# Constraints:
#
#
# 	3 <= n <= 105
# 	2 <= edges.length <= 105
# 	edges[i].length == 2
# 	1 <= ai, bi <= n
# 	ai != bi
# 	There are no repeated edges.
#
#


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        dd = defaultdict(set)
        for a, b in edges:
            dd[a].add(b)
            dd[b].add(a)
        
        odd = []
        for i in range(1, n + 1):
            if len(dd[i]) % 2:
                if len(dd[i]) == n - 1:
                    return False
                odd.append((i, dd[i]))
        if not odd: return True
                
        odd.sort(key=lambda x: len(x[1]), reverse=True)
        print(odd)
        if len(odd) == 2:
            a, b = [x[0] for x in odd]
            return a not in dd[b] or any([a not in dd[i] and b not in dd[i] for i in range(1, n + 1) if i != a and i != b])
            
        elif len(odd) == 4:
            a, b, c, d = [x[0] for x in odd]
            return any([
                a not in dd[b] and c not in dd[d],
                a not in dd[c] and b not in dd[d],
                a not in dd[d] and b not in dd[c]
            ])
        else:
            return False

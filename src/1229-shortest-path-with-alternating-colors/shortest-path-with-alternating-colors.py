# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
#
# 	redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# 	blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
#
#
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
#
#  
# Example 1:
#
#
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
#
#
# Example 2:
#
#
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 100
# 	0 <= redEdges.length, blueEdges.length <= 400
# 	redEdges[i].length == blueEdges[j].length == 2
# 	0 <= ai, bi, uj, vj < n
#
#


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u,v in redEdges: adj_list[u].append((v, 0)) # 0 - red, 1 - blue
        for u,v in blueEdges: adj_list[u].append((v, 1))
            
        queue = deque([(0,0),(0,1)]) # (node, last_color), start with red and blue pills
        
        dist = [float(inf)] * n
        visited = set()
        level = 0
        while queue:
            for _ in range(len(queue)):
                node, last_color = queue.popleft()
                dist[node] = min(dist[node], level)

                for nei,edge_color in adj_list[node]:
                    if last_color != edge_color and (nei, edge_color) not in visited:
                        visited.add((nei, edge_color))
                        queue.append((nei, edge_color))
            level += 1
        
        return [d if d != float(inf) else -1 for d in dist]
    

# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#
#
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
#  
# Constraints:
#
#
# 	The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# 	The size of flights will be in range [0, n * (n - 1) / 2].
# 	The format of each flight will be (src, dst, price).
# 	The price of each flight will be in the range [1, 10000].
# 	k is in the range of [0, n - 1].
# 	There will not be any duplicated flights or self cycles.
#
#


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        deque_vert = deque([[src, 0, 0]])
        min_price = float('inf')
     
        for i, j, w in flights: 
            graph[i].append([j, w])

        while deque_vert:
            city, visited, price = deque_vert.popleft()

            if price <= min_price and visited <= K and city != dst:
                for neibh, price_neibh in graph[city]:
                     deque_vert.append([neibh, visited + 1, price + price_neibh])
            
            if city == dst:
                min_price = min(min_price, price)
                
        return min_price if min_price != float('inf') else -1

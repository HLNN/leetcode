# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#  
# Example 1:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#
#
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation: The graph is shown.
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 100
# 	0 <= flights.length <= (n * (n - 1) / 2)
# 	flights[i].length == 3
# 	0 <= fromi, toi < n
# 	fromi != toi
# 	1 <= pricei <= 104
# 	There will not be any multiple flights between two cities.
# 	0 <= src, dst, k < n
# 	src != dst
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

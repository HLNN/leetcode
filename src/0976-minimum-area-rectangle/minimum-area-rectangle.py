# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
#
# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
#
#  
# Example 1:
#
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#
#
# Example 2:
#
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= points.length <= 500
# 	points[i].length == 2
# 	0 <= xi, yi <= 4 * 104
# 	All the given points are unique.
#
#


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        ans = inf
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return ans if ans < float('inf') else 0
    
#         def point_4(a, b, c):
#             x, y = zip(a, b, c)
#             if len(set(x)) != 2 or len(set(y)) != 2:
#                 return (-1, -1), inf
#             xx, yy = reduce(lambda x, y: x ^ y, x), reduce(lambda x, y: x ^ y, y)
#             s = abs(sum(x) - 3 * xx) * abs(sum(y) - 3 * yy) // 4
#             return (xx, yy), s
        
#         point_set = set(map(tuple, points))
#         res = inf
#         for a, b, c in combinations(points, 3):
#             p4, s = point_4(a, b, c)
#             if p4 in point_set:
#                 res = min(res, s)
        
#         return res if res != inf else 0
    

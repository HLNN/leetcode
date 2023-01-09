# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
#
#  
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#
#
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	1 <= points.length <= 300
# 	points[i].length == 2
# 	-104 <= xi, yi <= 104
# 	All the points are unique.
#
#


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result
    

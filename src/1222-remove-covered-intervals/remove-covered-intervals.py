# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.
#
#  
# Example 1:
#
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1
#
#
# Example 3:
#
#
# Input: intervals = [[0,10],[5,12]]
# Output: 2
#
#
# Example 4:
#
#
# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2
#
#
# Example 5:
#
#
# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= intervals.length <= 1000
# 	intervals[i].length == 2
# 	0 <= li <= ri <= 105
# 	All the given intervals are unique.
#
#


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        right, res, n = -1, 0, len(intervals)
        for _, end in intervals:
            if end <= right:
                res += 1
            else:
                right = end
        return n - res
    

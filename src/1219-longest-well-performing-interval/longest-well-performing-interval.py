# We are given hours, a list of the number of hours worked per day for a given employee.
#
# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
#
# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
#
# Return the length of the longest well-performing interval.
#
#  
# Example 1:
#
#
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
#
#
# Example 2:
#
#
# Input: hours = [6,6,6]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= hours.length <= 104
# 	0 <= hours[i] <= 16
#
#


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        wp = [0] + list(accumulate([1 if h > 8 else -1 for h in hours]))
        dd = defaultdict(lambda: inf)
        for i in range(len(wp) - 1, -1, -1):
            dd[wp[i]] = i
        
        # idx = len(wp)
        # for k in sorted(dd.keys()):
        #     idx = min(idx, dd[k])
        #     dd[k] = idx
        # return max(0, max(j - dd[h - 1] for j, h in enumerate(wp)))

        return max(0, max(j if h > 0 else (j - dd[h - 1]) for j, h in enumerate(wp)))
    

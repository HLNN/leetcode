# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
#
# A subarray is a contiguous part of an array.
#
#  
# Example 1:
# Input: nums = [1], k = 1
# Output: 1
# Example 2:
# Input: nums = [1,2], k = 4
# Output: -1
# Example 3:
# Input: nums = [2,-1,2], k = 3
# Output: 3
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 105
# 	-105 <= nums[i] <= 105
# 	1 <= k <= 109
#
#


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        q = deque()
        ans = inf
        for i, v in enumerate(s):
            while q and v - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and s[q[-1]] >= v:
                q.pop()
            q.append(i)
        return -1 if ans == inf else ans
    

# You are given an integer array nums and two integers indexDiff and valueDiff.
#
# Find a pair of indices (i, j) such that:
#
#
# 	i != j,
# 	abs(i - j) <= indexDiff.
# 	abs(nums[i] - nums[j]) <= valueDiff, and
#
#
# Return true if such pair exists or false otherwise.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
#
#
# Example 2:
#
#
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
#
#
#  
# Constraints:
#
#
# 	2 <= nums.length <= 105
# 	-109 <= nums[i] <= 109
# 	1 <= indexDiff <= nums.length
# 	0 <= valueDiff <= 109
#
#


from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])
            pos1 = bisect_left(SList, nums[i] - t)
            pos2 = bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
            
        return False
    

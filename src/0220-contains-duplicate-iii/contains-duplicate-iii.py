# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
#
#  
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 2 * 104
# 	-231 <= nums[i] <= 231 - 1
# 	0 <= k <= 104
# 	0 <= t <= 231 - 1
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
    

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid - 1] < target < nums[mid]:
                return mid
            elif nums[mid] < target < nums[mid + 1]:
                return mid + 1
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#  
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 105
# 	-109 <= nums[i] <= 109
# 	nums is a non-decreasing array.
# 	-109 <= target <= 109
#
#


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, ml, m, mr, r = 0, 0, 0, 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ml = mr = m
                while l <= ml:
                    m = (l + ml) // 2
                    if nums[m] == target:
                        ml = m
                        if m == 0 or nums[m - 1] < target:
                            break
                    else:
                        l = m + 1
                while mr <= r:
                    m = (mr + r + 1) // 2
                    if nums[m] == target:
                        mr = m
                        if m == len(nums) - 1 or nums[m + 1] > target:
                            break
                    else:
                        r = m - 1
                return [ml, mr]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [-1, -1]
    

# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
#
# Example 2:
#
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
#
# Example 3:
#
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 105
# 	-231 <= nums[i] <= 231 - 1
#
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 in range(n) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return next((i + 1 for i, num in enumerate(nums) if num != i + 1), n + 1)
    

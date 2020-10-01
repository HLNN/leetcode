# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Follow up:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 in range(n) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return next((i + 1 for i, num in enumerate(nums) if num != i + 1), n + 1)
    

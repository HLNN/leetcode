# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
#
# Return the shortest such subarray and output its length.
#
#  
# Example 1:
#
#
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [1]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 104
# 	-105 <= nums[i] <= 105
#
#
#  
# Follow up: Can you solve it in O(n) time complexity?


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = len(nums) - 1, 0
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
            
        stack = []
        for i in range(len(nums))[::-1]:
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        print(r,l)
        return r - l + 1 if r - l > 0 else 0
    

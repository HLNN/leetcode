# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
#  
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
#
#  
# Constraints:
#
#
# 	2 <= n <= 3 * 104
# 	nums.length == n + 1
# 	1 <= nums[i] <= n
# 	All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
#
#  
# Follow up:
#
#
# 	How can we prove that at least one duplicate number must exist in nums?
# 	Can you solve the problem without modifying the array nums?
# 	Can you solve the problem using only constant, O(1) extra space?
# 	Can you solve the problem with runtime complexity less than O(n2)?
#
#


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare

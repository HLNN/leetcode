# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#  
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#  
# Constraints:
#
#
# 	2 <= nums.length <= 3 * 104
# 	-231 <= nums[i] <= 231 - 1
# 	Each integer in nums will appear twice, only two integers will appear once.
#
#


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
            
        x = xor & -xor
        res = 0
        for i in nums:
            if i & x != 0:
                res ^= i
        return [res, res ^ xor]
    

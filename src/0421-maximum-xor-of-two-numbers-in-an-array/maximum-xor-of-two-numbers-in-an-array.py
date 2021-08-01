# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
#
#  
# Example 1:
#
#
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
#
# Example 2:
#
#
# Input: nums = [0]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [2,4]
# Output: 6
#
#
# Example 4:
#
#
# Input: nums = [8,10,2]
# Output: 10
#
#
# Example 5:
#
#
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 105
# 	0 <= nums[i] <= 231 - 1
#
#


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans
    

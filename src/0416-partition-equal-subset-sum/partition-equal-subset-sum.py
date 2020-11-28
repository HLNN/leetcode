# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
#  
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 200
# 	1 <= nums[i] <= 100
#
#


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a = reduce(lambda a, num: a|(a<<num), nums, 1)
        return sum(nums)%2 == 0 and a & (1 << (sum(nums)//2)) != 0
    

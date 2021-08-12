# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
#  
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 105
# 	1 <= nums[i] <= n
#
#
#  
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Solution1
        # def swap(i, j):
        #     nums[i], nums[j] = nums[j], nums[i]
        #
        # for i in range(len(nums)):
        #     while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
        #         swap(i, nums[i] - 1)
        #
        # return [i + 1 for i, x in enumerate(nums) if i != x - 1]
        
        # Solution2
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        
        return [i + 1 for i, x in enumerate(nums) if x > 0]
    

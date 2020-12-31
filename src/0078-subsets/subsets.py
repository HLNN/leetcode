# Given an integer array nums, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
# 	All the numbers of nums are unique.
#
#


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
        
    def dfs(self, nums, i, sub):
        if i == len(nums):
            self.res.append(sub[:])
            return
        self.dfs(nums, i+1, sub)
        sub.append(nums[i])
        self.dfs(nums, i+1, sub)
        sub.pop()
        

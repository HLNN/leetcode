# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
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
        

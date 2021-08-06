# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
#  
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
#
#


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(n, ans, res):
            res.append(ans)
            for i in range(n, len(nums)):
                if i > n and nums[i] == nums[i-1]: continue
                dfs(i+1, ans+[nums[i]], res)
        
        res = []
        nums.sort()
        dfs(0, [], res)
        return res
    

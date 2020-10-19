# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#  
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#
#
#  
# Constraints:
#
#
# 	1 <= candidates.length <= 100
# 	1 <= candidates[i] <= 50
# 	1 <= target <= 30
#
#


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(nums, l, res, i, combination, s):
            if s == target:
                res.append(combination[:])
                return
            elif i == len(l) or s > target:
                return
            else:
                num = l[i]
                for n in range(min(nums[num], (target - s) // num)):
                    combination.append(num)
                    bt(nums, l, res, i+1, combination, s + (n+1) * num)
                for n in range(min(nums[num], (target - s) // num)):
                    combination.pop()
                bt(nums, l, res, i+1, combination, s)
                
        res = []
        nums = {}
        l = []
        for i in range(len(candidates)):
            num = candidates[i]
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                l.append(num)
                     
        bt(nums, l, res, 0, [], 0)
        return res

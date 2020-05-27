# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
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

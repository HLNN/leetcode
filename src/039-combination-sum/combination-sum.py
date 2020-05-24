# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(candidates, res, i, combination, s):
            if s == target:
                res.append(combination[:])
                return
            elif i == len(candidates) or s > target:
                return
            else:
                for n in range((target - s) // candidates[i]):
                    combination.append(candidates[i])
                    bt(candidates, res, i+1, combination, s + (n+1) * candidates[i])
                for n in range((target - s) // candidates[i]):
                    combination.pop()
                bt(candidates, res, i+1, combination, s)
                
        res = []
        bt(candidates, res, 0, [], 0)
        return res

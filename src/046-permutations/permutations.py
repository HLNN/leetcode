# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(nums, ans, res, used):
            if len(ans) == len(nums):
                res.append(ans[:])
                return
            for i in range(len(nums)):
                if i in used: 
                    continue
                ans.append(nums[i])
                used.add(i)
                bt(nums, ans, res, used)
                ans.pop()
                used.remove(i)
        res = []
        bt(nums, [], res, set())
        return res
            

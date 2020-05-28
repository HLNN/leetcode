# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def bt(nums, ans, res, candi):
            if len(ans) == len(nums):
                res.append(ans[:])
                return
            for (k, v) in zip(candi.keys(), candi.values()):
                if v == 0: 
                    continue
                ans.append(k)
                candi[k] -= 1
                bt(nums, ans, res, candi)
                ans.pop()
                candi[k] += 1
                
        res = []
        candi = {}
        for i in range(len(nums)):
            if nums[i] not in candi.keys():
                candi[nums[i]] = 1
            else:
                candi[nums[i]] += 1
        bt(nums, [], res, candi)
        return res
            

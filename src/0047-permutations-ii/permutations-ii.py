# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 8
# 	-10 <= nums[i] <= 10
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
            

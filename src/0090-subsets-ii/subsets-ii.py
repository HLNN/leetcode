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
        def bt(i, ans):
            if i == n: return res.append(ans[:])
            bt(i + 1, ans)
            for _ in range(s[l[i]]):
                ans.append(l[i])
                bt(i + 1, ans)
            for _ in range(s[l[i]]):
                ans.pop()
        
        res = []
        s = defaultdict(int)
        for num in nums: s[num] += 1
        
        l, n = list(s), len(s)
        bt(0, [])
        return res

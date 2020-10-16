# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
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

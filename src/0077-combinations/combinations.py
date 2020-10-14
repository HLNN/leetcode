# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 20
# 	1 <= k <= n
#
#


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def bt(i, x, ans):
            if i == n + 1 or len(ans) == k:
                self.res.append(ans[:])
                return
            bt(i + 1, x, ans + [i])
            if x > 0:
                bt(i + 1, x - 1, ans)            
        self.res = []
        bt(1, n - k, [])
        return self.res
    

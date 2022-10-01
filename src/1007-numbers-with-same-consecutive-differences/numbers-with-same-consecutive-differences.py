# Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.
#
# Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
#
#  
# Example 1:
#
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#  
# Constraints:
#
#
# 	2 <= n <= 9
# 	0 <= k <= 9
#
#


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        @lru_cache(None)
        def dfs(i, j):
            if j < 0 or j > 9 or (j == 0 and i == 1): return []
            if i == 1: return [str(j)]
            out = []
            for d in set([K, -K]):
                out += [s+str(j) for s in dfs(i-1, j+d)]
            return out
        if N == 1: return range(10)
        return chain(*[dfs(N, i) for i in range(10)])
    

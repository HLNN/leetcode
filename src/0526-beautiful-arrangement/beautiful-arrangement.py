# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
#
#
# 	perm[i] is divisible by i.
# 	i is divisible by perm[i].
#
#
# Given an integer n, return the number of the beautiful arrangements that you can construct.
#
#  
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 15
#
#


class Solution:
    def countArrangement(self, n: int) -> int:
        # return (1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679)[N - 1]
        
        def dfs(i, used):
            if i == 0:
                self.res += 1
                return
            for x in range(n):
                if not used[x] and ((x+1) % (i+1) == 0 or (i+1) % (x+1) == 0):
                    used[x] = True
                    dfs(i - 1, used)
                    used[x] = False
        
        self.res = 0
        self.used = [False] * n
        dfs(n - 1, self.used)
        return self.res
    

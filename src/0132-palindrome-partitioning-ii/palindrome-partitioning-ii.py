# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#  
# Example 1:
#
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 0
#
#
# Example 3:
#
#
# Input: s = "ab"
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 2000
# 	s consists of lower-case English letters only.
#
#


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dpCost = [n - i - 1 for i in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j == n - 1:
                        dpCost[i] = 0
                    elif dpCost[j+1] + 1 < dpCost[i]:
                        dpCost[i] = dpCost[j+1] + 1
        
        return dpCost[0]
    

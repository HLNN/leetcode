# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
#
# 	Insert a character
# 	Delete a character
# 	Replace a character
#
#
#  
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#  
# Constraints:
#
#
# 	0 <= word1.length, word2.length <= 500
# 	word1 and word2 consist of lowercase English letters.
#
#


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        if not word2: return len(word1)
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(m + 1):
            dp[0][i] = i
        
        for i, j in product(range(1, n + 1), range(1, m + 1)):
            dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
            
        return dp[-1][-1]
    

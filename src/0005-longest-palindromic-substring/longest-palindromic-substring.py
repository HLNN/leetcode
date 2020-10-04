# Given a string s, return the longest palindromic substring in s.
#
#  
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters (lower-case and/or upper-case),
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = -1
        m = 0
        if len(s) <= 1:
            return s
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]
        for j in range(len(s)):
            for i in range(j + 1):
                dp[i][j] = s[i] == s[j] and ((j - i <= 2) or dp[i + 1][j - 1])
                if dp[i][j]:
                    if j - i + 1 > m:
                        start = i
                        end = j
                        m = j - i + 1
        return s[start:end + 1]
    

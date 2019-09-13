# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
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
    

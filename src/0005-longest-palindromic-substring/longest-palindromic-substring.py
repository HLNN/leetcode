# Given a string s, return the longest palindromic substring in s.
#
#  
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters.
#
#


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        n, res = len(s), (0, 0)
        
        def expand(i, j):
            while 0 <= i <= j < n and s[i] == s[j]:
                    i, j = i - 1, j + 1
            return i, j
        
        for i in range(n):
            r1 = expand(i, i)
            r2 = expand(i, i + 1)
            res = max(res, r1, r2, key=lambda x: x[1] -x[0])
            
        return s[res[0] + 1:res[1]]
    

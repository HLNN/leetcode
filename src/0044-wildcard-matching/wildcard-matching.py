# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#
#
# 	'?' Matches any single character.
# 	'*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
#  
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
#
# Example 4:
#
#
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#
#
# Example 5:
#
#
# Input: s = "acdcb", p = "a*c?b"
# Output: false
#
#
#  
# Constraints:
#
#
# 	0 <= s.length, p.length <= 2000
# 	s contains only lowercase English letters.
# 	p contains only lowercase English letters, '?' or '*'.
#
#


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return True if s == '' else False
        if s == '':
            return True if p == '*' else False
        
        dp, dpLast = [False] * (len(s) + 1), [False] * (len(s) + 1)
        dpLast[0] = True
        
        for n in range(len(p)):
            if p[n] == '*':
                if n > 0 and p[n-1] == '*':
                    continue
                dp[0] = dpLast[0]
            else:
                dp[0] = False
            for i in range(len(s)):
                if p[n] == s[i] or p[n] == '?':
                    dp[i+1] = dpLast[i]
                elif p[n] == '*':
                    dp[i+1] = dp[i] or dpLast[i+1]
                else:
                    dp[i+1] = False    
            dp, dpLast = dpLast, dp
        return dpLast[-1]

# # Not good 42.83% 50.00%
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if p == '':
#             return True if s == '' else False
#         if s == '':
#             return True if p == '*' else False
        
#         dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
#         dp[0][0] = True
        
#         for pi in range(len(p)):
#             if p[pi] == '*':
#                 dp[pi+1][0] = dp[pi][0]
#             else:
#                 break
        
#         for pi in range(len(p)):
#             for si in range(len(s)):
#                 if p[pi] == '?' or p[pi] == s[si]:
#                     dp[pi+1][si+1] = dp[pi][si]
#                 elif p[pi] == '*':
#                     dp[pi+1][si+1] = dp[pi][si+1] or dp[pi+1][si]
#         return dp[-1][-1]

# # Space: O(n) solution 63.30% 100.00%
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if p == '':
#             return True if s == '' else False
#         if s == '':
#             return True if p == '*' else False
        
#         dp, dpLast = [False] * len(s), [False] * len(s)
#         star = [False] * len(s)
#         for n in range(len(p)):
#             if n > 0 and p[n] == '*' and p[n-1] == '*':
#                 continue
#             dp, dpLast = dpLast, dp
#             for i in range(len(s)):
#                 if p[n] == '*':
#                     star[i] = False
#                     if n == 0:
#                         dp[i] = True
#                     elif i == 0:
#                         if dpLast[i]:
#                             dp[i] = True
#                             star[i] = True
#                         else:
#                             dp[i] = False
#                     elif dp[i-1] or dpLast[i-1]:
#                         dp[i] = True
#                     elif dpLast[i]:
#                         dp[i] = True
#                         star[i] = True
#                     else:
#                         dp[i] = False
#                 elif p[n] == '?':
#                     if n == 0 and i == 0:
#                         dp[i] = True
#                     elif i == 0:
#                         dp[i] = True if p[n-1] == '*' and dpLast[i] and not star[i] else False
#                     elif n > 0 and i > 0:
#                         dp[i] = True if dpLast[i-1] else False
#                     else:
#                         dp[i] = False
#                 else:
#                     if p[n] == s[i]:
#                         if n == 0 and i == 0:
#                             dp[i] = True
#                         elif i == 0:
#                             dp[i] = True if p[n-1] == '*' and dpLast[i] and not star[i] else False
#                         elif n > 0:
#                             dp[i] = True if dpLast[i-1] else False
#                     else:
#                         dp[i] = False
#         return dp[-1]

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
#
#  
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 3 * 104
# 	s[i] is '(', or ')'.
#
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 if i < 2 else dp[i - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] >= 2:
                        dp[i] += dp[i - dp[i - 1] - 2]
        return max(dp)
            
        

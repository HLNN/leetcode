# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
#  
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: s = "{[]}"
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of parentheses only '()[]{}'.
#
#


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        
        l = []
        n = -1
        
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                l.append(s[i])
                n += 1
            else:
                if n >= 0 and l[n] == pair[s[i]]:
                    l.pop()
                    n -= 1
                else:
                    return False
        if l:
            return False
        else:
            return True

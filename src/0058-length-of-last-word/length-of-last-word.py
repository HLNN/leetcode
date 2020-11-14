# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.
#
#  
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Example 2:
# Input: s = " "
# Output: 0
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of only English letters and spaces ' '.
#
#


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        f, res = True, 0
        for i in range(len(s) - 1, -1,-1):
            if s[i] == " ":
                if f:
                    continue
                else:
                    return res
            else:
                f = False
                res += 1
        return res

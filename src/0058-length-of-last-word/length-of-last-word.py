# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#  
# Example 1:
#
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The words are "Hello" and "World", both of length 5.
#
#
# Example 2:
#
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The longest word is "moon" with length 4.
#
#
# Example 3:
#
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The longest word is "joyboy" with length 6.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of only English letters and spaces ' '.
# 	There will be at least one word in s.
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

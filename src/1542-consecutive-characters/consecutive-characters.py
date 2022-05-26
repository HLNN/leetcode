# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
#
# Given a string s, return the power of s.
#
#  
# Example 1:
#
#
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
#
#
# Example 2:
#
#
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 500
# 	s consists of only lowercase English letters.
#
#


class Solution:
    def maxPower(self, s: str) -> int:
        # One line solution, using groupby
        # return max([len(list(x)) for _, x in groupby(s)])
        
        res, ans, lastChar = 0, 0, ""
        for c in s:
            if c == lastChar:
                ans += 1
            else:
                res = max(res, ans)
                ans, lastChar = 1, c
        return max(res, ans)
    

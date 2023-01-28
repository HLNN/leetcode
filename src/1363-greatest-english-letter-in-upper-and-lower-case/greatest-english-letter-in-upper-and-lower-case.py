# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
#
# An English letter b is greater than another letter a if b appears after a in the English alphabet.
#
#  
# Example 1:
#
#
# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.
#
#
# Example 2:
#
#
# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
#
#
# Example 3:
#
#
# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consists of lowercase and uppercase English letters.
#
#


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)

        for i in range(26, -1, -1):
            if chr(97 + i) in s and chr(65 + i) in s:
                return chr(65 + i)
        
        return ''
    

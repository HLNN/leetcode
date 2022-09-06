# Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
#
#
# 	For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
#
#
# Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.
#
# Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
#
#  
# Example 1:
#
#
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#
#
# Example 2:
#
#
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
#
#
# Example 3:
#
#
# Input: s = "LEETCODE"
# Output: 92
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 105
# 	s consists of uppercase English letters only.
#
#


def toIndex(s: str) -> int:
    return ord(s) - ord("A")


# Time: O(n)
# Space: O(1)
#
# Leveling idea:
#                     B
#           C       C B
#   B     B C     B C B
# A B   A B C   A B C B
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        contribution = [0] * 26
        lastLevel = [0] * 26
        res = 0
        curr = 0

        for i, c in enumerate(s):
            # Array index for the current character
            ci = toIndex(c)
            # The new character is stacked to the right of previous substrings.
            # The level refers to the height of that stack.
            currentLevel = i + 1

            # Calculate unique characters for current substrings
            # Formula: curr[i] = curr[i-1] - contribution[c] + new_contribution[c]
            curr -= contribution[ci]
            contribution[ci] = currentLevel - lastLevel[ci]
            curr += contribution[ci]
            lastLevel[ci] = currentLevel

            # Add unique characters derived from the current substrings to total
            res += curr
        
        return res
    

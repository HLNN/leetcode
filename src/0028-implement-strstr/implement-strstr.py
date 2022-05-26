# Implement strStr().
#
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
#  
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
#  
# Constraints:
#
#
# 	1 <= haystack.length, needle.length <= 104
# 	haystack and needle consist of only lowercase English characters.
#
#


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            f = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    f = False
                    break
            if f:
                return i
        return -1

# Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
#  
# Example 1:
#
#
# Input: s = "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
#
#
# Example 3:
#
#
# Input: s = "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 2000
# 	s consists of lowercase English letters.
#
#


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * 26

        for c in s:
            dp[ord(c) - 97] = sum(dp) + 1
        
        return sum(dp) % 1000000007
    

# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
#
#  
# Example 1:
#
#
# Input: s = "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: s = "cbacdcbc"
# Output: "acdb"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consists of lowercase English letters.
#
#
#  
# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        
        stack = []
        seen = set()
        for i, c in enumerate(s):
            while stack and c < stack[-1] and i < last[stack[-1]] and c not in seen:
                seen.remove(stack.pop())
            if c not in seen:
                seen.add(c)
                stack.append(c)
        
        return ''.join(stack)
    

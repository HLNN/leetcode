# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
#
#
# 	For example, the beauty of "abaacc" is 3 - 1 = 2.
#
#
# Given a string s, return the sum of beauty of all of its substrings.
#
#  
# Example 1:
#
#
# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
#
# Example 2:
#
#
# Input: s = "aabcbaa"
# Output: 17
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
    def beautySum(self, s: str) -> int:
        cnt = [[0] * 26]

        for c in s:
            cnt.append(cnt[-1].copy())
            cnt[-1][ord(c) - 97] += 1
        
        res = 0
        for j in range(1, len(s)):
            for i in range(j):
                diff = [b - a for a, b in zip(cnt[i], cnt[j + 1]) if a != b]
                res += max(diff) - min(diff)

        return res
    

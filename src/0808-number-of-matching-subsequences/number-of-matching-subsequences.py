# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
#
# 	For example, "ace" is a subsequence of "abcde".
#
#
#  
# Example 1:
#
#
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
#
#
# Example 2:
#
#
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 5 * 104
# 	1 <= words.length <= 5000
# 	1 <= words[i].length <= 50
# 	s and words[i] consist of only lowercase English letters.
#
#


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        
        res, n = len(words), len(s)
        for word in words:
            last = -1
            for c in word:
                idxs = d[c]
                i = bisect_right(idxs, last)
                if i < len(idxs):
                    last = idxs[i]
                else:
                    res -= 1
                    break
        
        return res
    

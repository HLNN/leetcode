# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
#
# You can return the answer in any order.
#
#  
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	1 <= words.length <= 5000
# 	1 <= words[i].length <= 30
# 	s and words[i] consist of lowercase English letters.
#
#


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        res = []
        wordLen = len(words[0])
        for start in range(wordLen):
            l = r = start
            need = words[:]
            while r < len(s):
                word = s[r: r + wordLen]
                if word not in words:
                    l = r = r + wordLen
                    need = words[:]
                elif word not in need:
                    while(s[l: l + wordLen] != word):
                        need.append(s[l: l + wordLen])
                        l += wordLen
                    l += wordLen
                    r += wordLen
                else:
                    need.remove(word)
                    r += wordLen
                    if len(need) == 0:
                        res.append(l)
                        need.append(s[l: l + wordLen])
                        l += wordLen
        return res

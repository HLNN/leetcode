# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
#
# Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
#
#  
# Example 1:
# Input: s = "banana"
# Output: "ana"
# Example 2:
# Input: s = "abcd"
# Output: ""
#
#  
# Constraints:
#
#
# 	2 <= s.length <= 3 * 104
# 	s consists of lowercase English letters.
#
#


class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h, t, d = (1<<(8*M-8))%q, 0, 256

        dic = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            for j in dic[t]:
                if text[i+1:i+M+1] == text[j:j+M]:
                    return (True, text[j:j+M])
            dic[t].append(i+1)
        return (False, "")
    
    def longestDupSubstring(self, S: str) -> str:
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found
    

# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.
#
# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.
#
#  
# Example 1:
#
#
# Input: s1 = "ab", s2 = "ba"
# Output: 1
# Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
#
#
# Example 2:
#
#
# Input: s1 = "abc", s2 = "bca"
# Output: 2
# Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".
#
#
#  
# Constraints:
#
#
# 	1 <= s1.length <= 20
# 	s2.length == s1.length
# 	s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
# 	s2 is an anagram of s1.
#
#


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2: return 0
        seen = set((s1,))
        s1, n = list(s1), len(s1)
        
        # s_in_list, idx, k
        q = [(s1, 0, 0)]
        
        idxs = defaultdict(list)
        for i, c in enumerate(s2):
            idxs[c].append(i)
        
        while q:
            q_new = []
            for (s, i, k) in q:
                while s[i] == s2[i]:
                    i += 1
                    if i == n: return k
                
                for j in idxs[s[i]]:
                    if j < i: continue
                    ss = s[:]
                    ss[i], ss[j] = ss[j], ss[i]
                    
                    ii, kk = i, k + 1
                    while ss[ii] == s2[ii]:
                        ii += 1
                        if ii == n: return kk
                    
                    s_str = ''.join(ss)
                    if s_str not in seen:
                        seen.add(s_str)
                        q_new.append((ss, ii, kk))
            q = q_new
    

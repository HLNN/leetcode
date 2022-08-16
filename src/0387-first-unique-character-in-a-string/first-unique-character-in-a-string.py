# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
#  
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 105
# 	s consists of only lowercase English letters.
#
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        seen_rep = set()
        
        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            else:
                seen_rep.add(c)
        
        res = len(s)
        for k, v in seen.items():
            if k not in seen_rep:
                res = min(res, v)
        
        return res if res < len(s) else -1
        
#         chars = defaultdict(list)
#         for i, c in enumerate(s):
#             chars[c].append(i)
        
#         res = len(s)
        
#         for c, idxs in chars.items():
#             if len(idxs) == 1:
#                 res = min(res, idxs[0])
        
#         return res if res < len(s) else -1
    

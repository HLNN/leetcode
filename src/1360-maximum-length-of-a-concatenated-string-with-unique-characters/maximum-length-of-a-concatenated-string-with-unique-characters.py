# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#
#  
# Example 1:
#
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
#
#
# Example 2:
#
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
#
#
# Example 3:
#
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 16
# 	1 <= arr[i].length <= 26
# 	arr[i] contains only lowercase English letters.
#
#


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [num for num in arr if len(str(num)) == len(set(str(num)))]
        bms = [reduce(lambda x, y: x | y, [1 << ord(c) - 97 for c in str(num)]) for num in arr]
        
        # @cache
        def bt(i, bm, prev):
            if i == len(arr): return prev
            res = 0
            if bm & bms[i] == 0:
                res = max(res, bt(i + 1, bm | bms[i], prev + len(arr[i])))
            res = max(res, bt(i + 1, bm, prev))
            return res
        
        return bt(0, 0, 0)
    

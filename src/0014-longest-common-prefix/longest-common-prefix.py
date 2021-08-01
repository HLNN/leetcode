# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#  
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#  
# Constraints:
#
#
# 	1 <= strs.length <= 200
# 	0 <= strs[i].length <= 200
# 	strs[i] consists of only lower-case English letters.
#
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        low = 1
        high = min(len(s) for s in strs)
        while low <= high:
            middle = (low + high) // 2
            if (self.isCommon(strs, middle)):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][0:(low + high) // 2]

    def isCommon(self, strs, l):
        subStr = strs[0][0:l]
        for s in strs:
            if not s[0:l] == subStr:
                return False
        return True

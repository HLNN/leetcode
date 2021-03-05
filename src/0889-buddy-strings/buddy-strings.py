# Given two strings a and b, return true if you can swap two letters in a so the result is equal to b, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at a[i] and b[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
#  
# Example 1:
#
#
# Input: a = "ab", b = "ba"
# Output: true
# Explanation: You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.
#
#
# Example 2:
#
#
# Input: a = "ab", b = "ab"
# Output: false
# Explanation: The only letters you can swap are a[0] = 'a' and a[1] = 'b', which results in "ba" != b.
#
#
# Example 3:
#
#
# Input: a = "aa", b = "aa"
# Output: true
# Explanation: You can swap a[0] = 'a' and a[1] = 'a' to get "aa", which is equal to b.
#
#
# Example 4:
#
#
# Input: a = "aaaaaaabc", b = "aaaaaaacb"
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= a.length, b.length <= 2 * 104
# 	a and b consist of lowercase letters.
#
#


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        x, diff = 0, [0, 0]
        for i in range(len(A)):
            if A[i] != B[i]:
                if x > 1: return False
                diff[x] = i
                x += 1
        if x == 0:
            s = set()
            for c in A:
                if c in s: return True
                s.add(c)
        return False if x != 2 or A[diff[0]] != B[diff[1]] or A[diff[1]] != B[diff[0]] else True
    

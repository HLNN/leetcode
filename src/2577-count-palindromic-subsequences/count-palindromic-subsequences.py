# Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.
#
# Note:
#
#
# 	A string is palindromic if it reads the same forward and backward.
# 	A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
#
#
#  
# Example 1:
#
#
# Input: s = "103301"
# Output: 2
# Explanation: 
# There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
# Two of them (both equal to "10301") are palindromic.
#
#
# Example 2:
#
#
# Input: s = "0000000"
# Output: 21
# Explanation: All 21 subsequences are "00000", which is palindromic.
#
#
# Example 3:
#
#
# Input: s = "9999900000"
# Output: 2
# Explanation: The only two palindromic subsequences are "99999" and "00000".
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of digits.
#
#


class Solution:
    def countPalindromes(self, s: str) -> int:
        one = defaultdict(int)
        two = defaultdict(int)
        one[int(s[-1])] = 1
        n = len(s)
        
        for i in range(n - 2, 2, -1):
            x = int(s[i])
            for xx in range(10):
                two[xx * 10 + x] += one[xx]
            one[x] += 1
        
        
        one2 = defaultdict(int)
        two2 = defaultdict(int)
        one2[int(s[0])] = 1
        res = 0
        
        for i in range(1, n-2):
            x = int(s[i])
            for xx in range(10):
                two2[xx * 10 + x] += one2[xx]
            one2[x] += 1
            
            for mid in range(100):
                res += two[mid] * two2[mid]
            
            x = int(s[i + 2])
            one[x] -= 1
            for xx in range(10):
                two[xx * 10 + x] -= one[xx]
        
        return res % 1000000007
                

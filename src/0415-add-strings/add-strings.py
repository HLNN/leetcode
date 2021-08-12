# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
#
#  
# Example 1:
#
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
#
# Example 2:
#
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
#
# Example 3:
#
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
#  
# Constraints:
#
#
# 	1 <= num1.length, num2.length <= 104
# 	num1 and num2 consist of only digits.
# 	num1 and num2 don't have any leading zeros except for the zero itself.
#
#


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r, n, res = 0, min(len(num1), len(num2)), ''
        
        for i in range(1, n+1):
            s = int(num1[-i]) + int(num2[-i]) + r
            r, s = divmod(s, 10)
            res += str(s)
        
        num, i = num1[:-n][::-1] or num2[:-n][::-1], 0
        
        while r and i < len(num):
            r, s = divmod(int(num[i]) + r, 10)
            res += str(s)
            i += 1
        
        res += num[i:]
        res += str(r) if r else ''
        
        return res[::-1]
    

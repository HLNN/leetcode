# Given an integer n, return true if n is an ugly number.
#
# Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
#
#  
# Example 1:
#
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
#
# Input: n = 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
#
# Example 3:
#
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.
#
#
# Example 4:
#
#
# Input: n = 1
# Output: true
# Explanation: 1 is typically treated as an ugly number.
#
#
#  
# Constraints:
#
#
# 	-231 <= n <= 231 - 1
#
#


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        while num % 5 == 0:
            num //= 5
        while num % 3 == 0:
            num //= 3
        while num % 2 == 0:
            num //= 2
        return num == 1
        

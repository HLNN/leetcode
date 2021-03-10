# Given an integer n, return the nth ugly number.
#
# Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.
#
#  
# Example 1:
#
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
# Explanation: 1 is typically treated as an ugly number.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 1690
#
#


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
    

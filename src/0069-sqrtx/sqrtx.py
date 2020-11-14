# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
#  
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
#  
# Constraints:
#
#
# 	0 <= x <= 231 - 1
#
#


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 4:
            if x == 0:
                return 0
            else:
                return 1
        else:
            l = 2
            r = x // 2
            while r - l > 1:
                m = (l + r) // 2
                m2 = m * m
                if m2 == x:
                    return m
                elif m2 > x:
                    r = m
                else:
                    l = m
            r2 = r * r
            if x == r2:
                return r
            else:
                return l

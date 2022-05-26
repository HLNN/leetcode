# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#  
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
#


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483648:
            return 0
        f = 1
        if x < 0:
            f = -1
        y = f * int(str(abs(x))[::-1])
        if y > 2147483647 or y < -2147483648:
            return 0
        else:
            return y

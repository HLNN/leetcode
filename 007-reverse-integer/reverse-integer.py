# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
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

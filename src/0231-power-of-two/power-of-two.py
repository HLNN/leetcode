# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true 
# Explanation: 20 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        b = str(bin(n))[2:]
        for i in range(1, len(b)):
            if b[i] == '1':
                return False
        return True

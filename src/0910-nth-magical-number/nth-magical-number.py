# A positive integer is magical if it is divisible by either a or b.
#
# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: n = 1, a = 2, b = 3
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 4, a = 2, b = 3
# Output: 6
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 109
# 	2 <= a, b <= 4 * 104
#
#


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        c = lcm(a, b)
        m = c // a + c // b - 1
        r = n % m
        res = c * (n // m) % MOD
        if r == 0:
            return res
        addA = a
        addB = b
        for _ in range(r - 1):
            if addA < addB:
                addA += a
            else:
                addB += b
        return (res + min(addA, addB) % MOD) % MOD
    

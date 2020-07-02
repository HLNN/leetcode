# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n)) ** 2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j)) ** 2 == n - j*j: return 2
        
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7: return 4
        return 3
    

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
#
#  
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
#
#  
# Constraints:
#
#
# 	-231 <= dividend, divisor <= 231 - 1
# 	divisor != 0
#
#


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def overflow(x):
            if x > 2147483647:
                return 2147483647
            elif x < -2147483648:
                return -2147483648
            else:
                return x
            
        if dividend == 0:
            return 0
        if divisor == 1:
            return overflow(dividend)
        if divisor == -1:
            return overflow(-dividend)
        
        neg = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            neg = True
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        
        base = [divisor]
        while base[-1] + base[-1] <= dividend:
            base.append(base[-1] + base[-1])
        result = 0
        for i in range(len(base) - 1, -1, -1):
            result += result
            if dividend >= base[i]:
                result += 1
                dividend -= base[i]
                 
        if neg:
            return -overflow(result)
        else:
            return overflow(result)
        
        
    

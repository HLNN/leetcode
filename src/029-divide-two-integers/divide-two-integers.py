# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
#
#
# Note:
#
#
# 	Both dividend and divisor will be 32-bit signed integers.
# 	The divisor will never be 0.
# 	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
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
        
        
    

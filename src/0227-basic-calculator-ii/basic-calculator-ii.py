# Given a string s which represents an expression, evaluate this expression and return its value. 
#
# The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#  
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 3 * 105
# 	s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# 	s represents a valid expression.
# 	All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# 	The answer is guaranteed to fit in a 32-bit integer.
#
#


class Solution:
    def calculate(self, s: str) -> int:
        print(s)
        def getOpe(g):
            for i in g:
                if i != " ": return i
        
        opes, nums = [], []
        for num, g in groupby(list(s), key=lambda x: "0" <= x <= "9"):
            g = list(g)
            if num:
                if opes and opes[-1] in "*/":
                    ope = opes.pop()
                    if ope == "*":
                        nums.append(nums.pop() * int("".join(g)))
                    else:
                        nums.append(nums.pop() // int("".join(g)))
                else:
                    nums.append(int("".join(g)))
            else:
                ope = getOpe(g)
                if ope: opes.append(ope)
        
        res = nums[0]
        for i in range(len(opes)):
            if opes[i] == "-":
                res -= nums[i + 1]
            else:
                res += nums[i + 1]
        return res
    

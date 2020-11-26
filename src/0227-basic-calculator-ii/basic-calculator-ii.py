# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
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
    

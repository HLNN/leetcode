# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#
#


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += " "
        res, op, stack = 0, None, []
        num = None
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                if num != None:
                    num *= 10
                    num += int(s[i])
                else:
                    num = int(s[i])
            else:
                if num != None:
                    res = self.arithmetic(res, op, num)
                    num = None
                if ch in ["+", "-"]:
                    op = ch
                elif ch == "(":
                    stack.extend([op, res])
                    res, op = 0, None
                elif ch == ")":
                    res = self.arithmetic(stack.pop(), stack.pop(), res)
        return res
    
    
    def arithmetic(self, res, op, num):
        if not op:
            res = num
        else:
            res += num * [-1, 1][(op == "+") * 1]
        return res

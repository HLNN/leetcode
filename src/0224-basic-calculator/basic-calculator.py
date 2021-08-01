# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#  
# Example 1:
#
#
# Input: s = "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: s = " 2-1 + 2 "
# Output: 3
#
#
# Example 3:
#
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 3 * 105
# 	s consists of digits, '+', '-', '(', ')', and ' '.
# 	s represents a valid expression.
# 	'+' is not used as a unary operation.
# 	'-' could be used as a unary operation but it has to be followed by parentheses.
# 	Every number and running calculation will fit in a signed 32-bit integer.
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

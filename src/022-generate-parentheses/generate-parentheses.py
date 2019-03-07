#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrace(s = "", left = 0, right = 0):
            if len(s) == 2 * n:
                output.append(s)
            if left < n:
                backtrace(s + "(", left + 1, right)
            if right < left:
                backtrace(s + ")", left, right + 1)
                
        backtrace()
        return output

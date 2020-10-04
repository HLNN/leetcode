# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#  
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#  
# Constraints:
#
#
# 	1 <= n <= 8
#
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

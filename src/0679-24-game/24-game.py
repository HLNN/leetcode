#
# You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use - as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#
#
#


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x] + rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a+b, a-b, a*b, b and a/b})
    

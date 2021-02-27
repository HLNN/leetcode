# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#  
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        # Catelan number
        res = 1
        for i in range(n + 1, 2 * n + 1):
            res = res * i // (i - n)
        return res // (n + 1)
    

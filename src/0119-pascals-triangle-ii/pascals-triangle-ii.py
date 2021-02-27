# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#  
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
#  
# Constraints:
#
#
# 	0 <= rowIndex <= 33
#
#
#  
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        res = [1]
        for i in range(1, rowIndex+1):
            row, res = res, [0] * (i + 1)
            res[0] = res[-1] = 1
            for j in range(1, i):
                res[j] = row[j] + row[j-1]
        return res

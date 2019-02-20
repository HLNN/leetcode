# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        zig = [""] * numRows
        loc = self.location(numRows - 1)
        for c, l in zip(s, loc):
            zig[l] += c
        return "".join(zig)
    
    def location(self, bound):
        index, inc = 0, 1
        while True:
            yield index;
            if index == bound:
                inc = -1
            elif index == 0:
                    inc = 1
            index += inc
        

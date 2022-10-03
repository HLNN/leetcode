# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
#
#  
# Example 1:
#
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
#
# Example 2:
#
#
# Input: start = "X", end = "L"
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= start.length <= 104
# 	start.length == end.length
# 	Both start and end will only consist of characters in 'L', 'R', and 'X'.
#
#


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j, n = 0, 0, len(start)

        while i < n and j < n:
            while i < n and start[i] == 'X': i += 1
            while j < n and end[j] == 'X': j += 1

            if i < n and j < n:
                if start[i] != end[j] or start[i] == 'L' and i < j or start[i] == 'R' and i > j: return False
                i += 1
                j += 1
        
        if i < n: return not any(c != 'X' for c in start[i:])
        if j < n: return not any(c != 'X' for c in end[j:])

        return True
    

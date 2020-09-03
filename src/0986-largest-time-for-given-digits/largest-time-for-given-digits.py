# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
#
#  
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#  
#
# Note:
#
#
# 	A.length == 4
# 	0 <= A[i] <= 9
#
#
#


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        res = ""
        for p in permutations(A):
            if p[0]*10 + p[1] < 24 and p[2] < 6:
                res = max(res, str(p[0]) + str(p[1]) + ":" + str(p[2]) + str(p[3]))
        return res
    

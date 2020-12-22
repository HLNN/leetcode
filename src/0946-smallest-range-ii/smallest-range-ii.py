# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
#
# After this process, we have some array B.
#
# Return the smallest possible difference between the maximum value of B and the minimum value of B.
#
#  
#
#
#
#
#
# Example 1:
#
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
#
#
#
# Example 2:
#
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
#
#
#
# Example 3:
#
#
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 10000
# 	0 <= A[i] <= 10000
# 	0 <= K <= 10000
#
#
#
#


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        n, ans = len(A), float("inf")

        for i in range(n-1):
            cands = [A[0], A[i], A[i+1] - 2*K, A[-1] - 2*K]
            ans = min(ans, max(cands) - min(cands))
            
        return min(ans, A[-1] - A[0])
    

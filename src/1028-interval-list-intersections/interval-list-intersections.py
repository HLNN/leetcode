# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
#
#  
# Example 1:
#
#
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
# Example 2:
#
#
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
#
#
#  
# Constraints:
#
#
# 	0 <= firstList.length, secondList.length <= 1000
# 	firstList.length + secondList.length >= 1
# 	0 <= starti < endi <= 109
# 	endi < starti+1
# 	0 <= startj < endj <= 109 
# 	endj < startj+1
#
#


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        a, b, n, m = 0, 0, len(A), len(B)
        
        while a < n and b < m:
            if A[a][0] > B[b][1]:
                b += 1
            elif B[b][0] > A[a][1]:
                a += 1
            else:
                res.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
                if A[a][1] < B[b][1]:
                    a += 1
                else:
                    b += 1
        
        return res
    

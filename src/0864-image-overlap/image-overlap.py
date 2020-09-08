# Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
#
# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
#
# (Note also that a translation does not include any kind of rotation.)
#
# What is the largest possible overlap?
#
# Example 1:
#
#
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
#
# Notes: 
#
#
# 	1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 	0 <= A[i][j], B[i][j] <= 1
#
#


from scipy.ndimage import convolve
import numpy as np

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
        return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))
    

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#  
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#  
# Constraints:
#
#
# 	nums1.length == m
# 	nums2.length == n
# 	0 <= m <= 1000
# 	0 <= n <= 1000
# 	1 <= m + n <= 2000
# 	-106 <= nums1[i], nums2[i] <= 106
#
#
#  
# Follow up: The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import sys
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)
        l = n + m
        cut1 = cut2 = cutL = 0
        cutR = len(nums1)
        while cut1 <= len(nums1):
            cut1 = (cutR - cutL) // 2 + cutL
            cut2 = l // 2 - cut1
            L1 = nums1[cut1 - 1] if cut1 != 0 else -sys.maxsize
            L2 = nums2[cut2 - 1] if cut2 != 0 else -sys.maxsize
            R1 = nums1[cut1] if cut1 != n else sys.maxsize
            R2 = nums2[cut2] if cut2 != m else sys.maxsize
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            else:
                if l % 2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1 + R1) / 2
                else:
                    R1 = min(R1, R2)
                    return R1

        

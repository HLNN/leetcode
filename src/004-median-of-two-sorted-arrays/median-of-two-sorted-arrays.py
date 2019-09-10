# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#


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

        

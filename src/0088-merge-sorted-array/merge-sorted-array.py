# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
#
#  
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
#  
# Constraints:
#
#
# 	nums1.length == m + n
# 	nums2.length == n
# 	0 <= m, n <= 200
# 	1 <= m + n <= 200
# 	-109 <= nums1[i], nums2[i] <= 109
#
#


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return
        if n == 0: return
        
        p1, p2, t = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[t] = nums1[p1]
                t -= 1
                p1 -= 1
            else:
                nums1[t] = nums2[p2]
                t -= 1
                p2 -= 1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1
        

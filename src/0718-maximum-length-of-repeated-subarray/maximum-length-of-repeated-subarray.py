# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
#
#  
# Example 1:
#
#
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
#
# Example 2:
#
#
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
#
#
#  
# Constraints:
#
#
# 	1 <= nums1.length, nums2.length <= 1000
# 	0 <= nums1[i], nums2[i] <= 100
#
#


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i, j in product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
        
        return max(chain(*dp))
    

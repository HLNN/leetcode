# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#
#
# 	The minimum value in the subarray is equal to minK.
# 	The maximum value in the subarray is equal to maxK.
#
#
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#
#  
# Example 1:
#
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
#
#
#  
# Constraints:
#
#
# 	2 <= nums.length <= 105
# 	1 <= nums[i], minK, maxK <= 106
#
#


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def count(s):
            
            # print(s)
            res = 0
            for i in range(len(s)):
                j = i
                # a, b = False, False
                # print(i, j)
                a, b = s[j] == minK, s[j] == maxK
                while not (a and b):
                    j += 1
                    if j == len(s): return res
                    a, b = a or s[j] == minK, b or s[j] == maxK
                # print(i, j)
                res += len(s) - j
            return res
        
        l, r, res = 0, 0, 0
        while r < len(nums):
            while l < len(nums) and not minK <= nums[l] <= maxK:
                l += 1
            r = l
            while r < len(nums) and minK <= nums[r] <= maxK:
                r += 1
            res += count(nums[l:r])
            l = r
        
        return res
                

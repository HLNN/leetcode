# Given an integer array nums, return the number of longest increasing subsequences.
#
# Notice that the sequence has to be strictly increasing.
#
#  
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2000
# 	-106 <= nums[i] <= 106
#
#


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        lengths = [0] * n
        counts = [1] * n
        
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
    

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
#  
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 104
# 	-1000 <= nums[i] <= 1000
# 	-107 <= k <= 107
#
#


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        pre_sum, res = 0, 0
        for num in nums:
            pre_sum += num
            res += sum_freq[pre_sum - k]
            sum_freq[pre_sum] += 1

        return res
    

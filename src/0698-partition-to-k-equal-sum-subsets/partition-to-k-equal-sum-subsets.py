# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
#
#  
# Example 1:
#
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= k <= nums.length <= 16
# 	1 <= nums[i] <= 104
# 	The frequency of each element is in the range [1, 4].
#
#


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def bt(k, bucket, nums, start, used, target):
            if k == 0: return True
            if bucket == target: return bt(k - 1, 0, nums, 0, used, target)

            for i in range(start, len(nums)):
                if used[i] or bucket + nums[i] > target: continue

                used[i] = True
                bucket += nums[i]
                if bt(k, bucket, nums, start + 1, used, target): return True
                used[i] = False
                bucket -= nums[i]

            return False
        
        if k > len(nums): return False
        s = sum(nums)
        if s % k != 0: return False

        nums.sort(reverse=True)
        target = s // k
        used = [False] * len(nums)

        return bt(k, 0, nums, 0, used, target)
    

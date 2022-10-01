# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#  
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
#  
# Constraints:
#
#
# 	3 <= nums.length <= 1000
# 	-1000 <= nums[i] <= 1000
# 	-104 <= target <= 104
#
#


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        
        nums.sort()
        closest = None
        closest_distance = float('inf')
        
        for i in range(len(nums[:-2])):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                elif current_sum == target:
                    return target
                
                current_distance = abs(current_sum - target)
                if current_distance < closest_distance:
                    closest = current_sum
                    closest_distance = current_distance
        
        return closest
            
        

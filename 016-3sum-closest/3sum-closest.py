# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
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
            
        

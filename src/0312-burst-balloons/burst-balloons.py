# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#  
# Example 1:
#
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
#
#
# Input: nums = [1,5]
# Output: 10
#
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 500
# 	0 <= nums[i] <= 100
#
#


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            return max([A[i]*A[k]*A[j] + dfs(i,k) + dfs(k,j) for k in range(i+1, j)] or [0])
        
        return dfs(0, len(A) - 1)
    

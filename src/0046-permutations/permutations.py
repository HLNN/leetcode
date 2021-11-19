# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#  
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 6
# 	-10 <= nums[i] <= 10
# 	All the integers of nums are unique.
#
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(x, ans):
            if x == n:
                res.append(ans)
            else:
                for i in range(n):
                    if not used[i]:
                        used[i] = True
                        bt(x + 1, ans + [nums[i]])
                        used[i] = False

        res, n = [], len(nums)
        used = [False] * n
        bt(0, [])
        return res
    

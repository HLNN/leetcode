# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
# Example 2:
#
#
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 15
# 	-100 <= nums[i] <= 100
#
#


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        def bt(i, ans):
            s = str(ans)
            if len(ans) > 1 and s not in seen:
                seen.add(s)
                res.append(ans[:])
            
            if i == len(nums): return
            
            bt(i + 1, ans)
            if not ans or nums[i] >= ans[-1]:
                ans.append(nums[i])
                bt(i + 1, ans)
                ans.pop()
        
        bt(0, [])
        return res
    

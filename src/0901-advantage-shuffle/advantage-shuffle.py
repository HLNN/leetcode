# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
#
# Return any permutation of nums1 that maximizes its advantage with respect to nums2.
#
#  
# Example 1:
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]
#
#  
# Constraints:
#
#
# 	1 <= nums1.length <= 105
# 	nums2.length == nums1.length
# 	0 <= nums1[i], nums2[i] <= 109
#
#


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = Counter(nums1)
        nums1.sort()
        nums2 = sorted((num, i) for i, num in enumerate(nums2))
        n = len(nums1)
        start, res = 0, {}

        for num, i in nums2:
            while start < n and nums1[start] <= num:
                start += 1
            if start < n:
                res[i] = nums1[start]
                nums[nums1[start]] -= 1
                start += 1
        
        nums = chain.from_iterable(repeat(num, t) for num, t in nums.items())

        return [res.get(i) if (i in res) else next(nums) for i in range(n)]
    

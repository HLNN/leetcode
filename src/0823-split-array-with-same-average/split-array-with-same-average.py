# You are given an integer array nums.
#
# You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).
#
# Return true if it is possible to achieve that and false otherwise.
#
# Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
#
#
# Example 2:
#
#
# Input: nums = [3,1]
# Output: false
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 30
# 	0 <= nums[i] <= 104
#
#


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)

        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False


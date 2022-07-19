# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# You must solve it in O(n) time complexity.
#
#  
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#  
# Constraints:
#
#
# 	1 <= k <= nums.length <= 105
# 	-104 <= nums[i] <= 104
#
#


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        if k <= len(nums):
            for i in range(k, len(nums)):
                if nums[i] > heap[0]:
                    heapq.heapreplace(heap, nums[i])
        return heap[0]

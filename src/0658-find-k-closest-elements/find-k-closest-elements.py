# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
#
# 	|a - x| < |b - x|, or
# 	|a - x| == |b - x| and a < b
#
#
#  
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#  
# Constraints:
#
#
# 	1 <= k <= arr.length
# 	1 <= arr.length <= 104
# 	arr is sorted in ascending order.
# 	-104 <= arr[i], x <= 104
#
#


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            if len(heap) < k:
                heappush(heap, (-abs(num - x), -num))
            else:
                heappushpop(heap, (-abs(num - x), -num))
                
        res = [-v for _, v in heap]
        res.sort()
        return res
    
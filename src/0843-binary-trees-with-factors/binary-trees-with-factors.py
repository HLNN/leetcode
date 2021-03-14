# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
#
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
#
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
#
# Example 2:
#
#
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 1000
# 	2 <= arr[i] <= 109
#
#


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        @lru_cache()
        def dp(i):
            res = 1
            l, r = 0, i - 1
            
            while l <= r:
                product = arr[l] * arr[r]
                if product == arr[i]:
                    res += dp(l) * dp(r) * (1 + int(arr[l] != arr[r]))
                    l, r = l + 1, r - 1
                elif product > arr[i]:
                    r -= 1
                else:
                    l += 1
            return res
        
        arr.sort()
        return sum(dp(i) for i in range(len(arr))) % (10 ** 9 + 7)
    

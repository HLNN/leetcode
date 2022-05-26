# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
#
# As the answer can be very large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
#
#
# Example 2:
#
#
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
# Example 3:
#
#
# Input: arr = [2,1,3], target = 6
# Output: 1
# Explanation: (1, 2, 3) occured one time in the array so we return 1.
#
#
#  
# Constraints:
#
#
# 	3 <= arr.length <= 3000
# 	0 <= arr[i] <= 100
# 	0 <= target <= 300
#
#


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = defaultdict(int)
        for i in arr: count[i] += 1
        res = 0
        
        for x in range(101):
            if not count[x]: continue
            
            # All different
            for y in range(x+1, 101):
                z = target - x - y
                if y < z < 101:
                    res += count[x] * count[y] * count[z]
            
            # x == y
            z = target - x*2
            if x < z < 101:
                res += count[x] * (count[x]-1) // 2 * count[z]
            
            # y == z
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y < 101:
                    res += count[x] * count[y] * (count[y]-1) // 2
        
        # x == y == z
        if target % 3 == 0:
            x = target // 3
            res += count[x] * (count[x]-1) * (count[x]-2) // 6
        
        return res % (10**9 + 7)
    

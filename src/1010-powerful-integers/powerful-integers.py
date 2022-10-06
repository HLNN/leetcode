# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
#
# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
#
# You may return the answer in any order. In your answer, each value should occur at most once.
#
#  
# Example 1:
#
#
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32
#
#
# Example 2:
#
#
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
#
#
#  
# Constraints:
#
#
# 	1 <= x, y <= 100
# 	0 <= bound <= 106
#
#


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0: return []
        
        a = 0 if x == 1 else int(log(bound, x))
        b = 0 if y == 1 else int(log(bound, y))
        
        res = set()
        for i, j in product(range(a + 1), range(b + 1)):
            value = x ** i + y ** j
            if value <= bound:
                res.add(value)
            
        return list(res)
    

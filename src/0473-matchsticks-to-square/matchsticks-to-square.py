# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#  
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
#
#
#  
# Constraints:
#
#
# 	1 <= matchsticks.length <= 15
# 	1 <= matchsticks[i] <= 108
#
#


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s, n = sum(matchsticks), len(matchsticks)
        if n < 4 or s % 4 != 0: return False
        
        matchsticks.sort(reverse=True)
        edge = s // 4
        
        @cache
        def bt(l1, l2, l3, l4, i):
            if i == n:
                return True if l1 == l2 == l3 == l4 == edge else False
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False
            
            return bt(l1 + matchsticks[i], l2, l3, l4, i + 1) or bt(l1, l2 + matchsticks[i] , l3, l4, i + 1) or bt(l1, l2, l3 + matchsticks[i], l4, i + 1) or bt(l1, l2, l3, l4 + matchsticks[i] , i + 1)
        
        return bt(0, 0, 0, 0, 0)
    
